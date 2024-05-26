import os
import random
import torch
from torch.utils.data import DataLoader, ConcatDataset, Subset
from torchvision import transforms
from efficientnet_pytorch import EfficientNet
from torch.optim.lr_scheduler import _LRScheduler
from dataload import CustomImageDataset  # 从 dataload.py 导入 CustomImageDataset
from tqdm import tqdm
from torch.utils.tensorboard import SummaryWriter
from ewc import EWC  # 导入 EWC 类

class WarmUpCosineDecayScheduler(_LRScheduler):
    def __init__(
        self,
        optimizer,
        warmup_steps,
        total_steps,
        base_lr,
        final_lr,
        warmup_lr=0.0,
        hold_base_rate_steps=0,
        last_epoch=-1,
    ):
        self.warmup_steps = warmup_steps
        self.total_steps = total_steps
        self.base_lr = base_lr
        self.final_lr = final_lr
        self.warmup_lr = warmup_lr
        self.hold_base_rate_steps = hold_base_rate_steps
        self.finished = False
        super(WarmUpCosineDecayScheduler, self).__init__(optimizer, last_epoch)

    def get_lr(self):
        if not self.finished:
            if self.last_epoch < self.warmup_steps:
                slope = (self.base_lr - self.warmup_lr) / self.warmup_steps
                return [self.warmup_lr + slope * self.last_epoch for _ in self.base_lrs]
            else:
                self.finished = True
        if self.last_epoch < self.warmup_steps + self.hold_base_rate_steps:
            return [self.base_lr for _ in self.base_lrs]
        cosine_decay = 0.5 * (
            1
            + np.cos(
                np.pi
                * (self.last_epoch - self.warmup_steps - self.hold_base_rate_steps)
                / (self.total_steps - self.warmup_steps - self.hold_base_rate_steps)
            )
        )
        return [
            self.final_lr + (self.base_lr - self.final_lr) * cosine_decay
            for _ in self.base_lrs
        ]

# 定义读取数据集的函数
def read_dataset(file_path):
    dataset = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            file_path, label = line.strip().split("\t")
            dataset.append((file_path, int(label)))
    return dataset

# 读取旧的训练集和增量数据集
train_dataset = read_dataset("train.txt")
incremental_dataset = read_dataset("incremental.txt")

# 定义数据转换
transform = transforms.Compose(
    [
        transforms.Resize((224, 224)),  # 调整图像尺寸为 224x224
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)

# 创建 CustomImageDataset
train_dataset = CustomImageDataset(label_file="train.txt", transform=transform)
incremental_dataset = CustomImageDataset(label_file="incremental.txt", transform=transform)

# 经验重放：选择部分旧的训练集
old_data_fraction = 0.1  # 使用 10% 的旧数据进行经验重放
old_data_size = int(len(train_dataset) * old_data_fraction)
old_data_indices = random.sample(range(len(train_dataset)), old_data_size)
old_data_subset = Subset(train_dataset, old_data_indices)

# 合并旧数据子集和增量数据集
combined_dataset = ConcatDataset([old_data_subset, incremental_dataset])
combined_loader = DataLoader(combined_dataset, batch_size=16, shuffle=True, num_workers=4)

# 加载之前训练好的模型
model_path = "checkpoints/final_model5.pth"
model = EfficientNet.from_name("efficientnet-b5")
num_ftrs = model._fc.in_features
model._fc = torch.nn.Linear(num_ftrs, len(set([label for _, label in combined_dataset])))
model.load_state_dict(torch.load(model_path))
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

# 定义损失函数和优化器
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 定义学习率调度器
warmup_steps = 10  # 设置 Warmup 步数
total_steps = len(combined_loader) * 10  # 总步数为 10 个 epoch
scheduler = WarmUpCosineDecayScheduler(
    optimizer,
    warmup_steps=warmup_steps,
    total_steps=total_steps,
    base_lr=0.001,
    final_lr=0.0001,
    warmup_lr=0.0,
)

# 初始化 TensorBoard
writer = SummaryWriter()

# 初始化 EWC
old_loader = DataLoader(old_data_subset, batch_size=16, shuffle=True, num_workers=4)
ewc = EWC(model, old_loader, device)

# 训练模型
num_epochs = 10
lambda_ewc = 0.1  # EWC 正则化项的权重

for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    combined_loader = tqdm(combined_loader, desc=f"Training Epoch {epoch+1}/{num_epochs}")
    for images, labels in combined_loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        ewc_loss = lambda_ewc * ewc.penalty(model)  # 计算 EWC 损失
        total_loss = loss + ewc_loss
        total_loss.backward()
        optimizer.step()

        running_loss += total_loss.item()
        scheduler.step()  # 更新学习率

    avg_train_loss = running_loss / len(combined_loader)
    writer.add_scalar('Loss/incremental_train', avg_train_loss, epoch)  # 记录增量训练损失

    print(
        f"Epoch {epoch+1}/{num_epochs}, "
        f"Incremental Train Loss: {avg_train_loss:.4f}"
    )

# 删除保存的中间模型
for filename in os.listdir("checkpoints"):
    file_path = os.path.join("checkpoints", filename)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(f"Failed to delete {file_path}. Reason: {e}")

# 保存最终增量学习后的模型
torch.save(model.state_dict(), os.path.join("checkpoints", "final_model_incremental.pth"))
writer.close()  # 关闭 TensorBoard 记录器
