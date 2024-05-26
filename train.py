import os
import numpy as np
import torch
from torch.utils.data import DataLoader
from torchvision import transforms
from sklearn.model_selection import train_test_split
from efficientnet_pytorch import EfficientNet
from dataset import CustomImageDataset
from torch.optim.lr_scheduler import _LRScheduler, CosineAnnealingLR

class WarmUpCosineDecayScheduler(_LRScheduler):
    def __init__(self, optimizer, warmup_steps, total_steps, base_lr, final_lr, warmup_lr=0.0, hold_base_rate_steps=0, last_epoch=-1):
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
        cosine_decay = 0.5 * (1 + np.cos(np.pi * (self.last_epoch - self.warmup_steps - self.hold_base_rate_steps) / (self.total_steps - self.warmup_steps - self.hold_base_rate_steps)))
        return [self.final_lr + (self.base_lr - self.final_lr) * cosine_decay for _ in self.base_lrs]

# 读取标签文件并创建标签字典
label_file = "label.txt"
label_dict = {}
with open(label_file, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("\t")
        pre = parts[0].strip().split("_")
        category = pre[1]  # 类别
        label = int(parts[1])  # 标签
        label_dict[category] = label

# 获取所有图片文件及其标签
upload_folder = "upload"
image_files = [f for f in os.listdir(upload_folder) if f.endswith(".jpeg")]
image_labels = []
for image_file in image_files:
    parts = image_file.split("_")
    category = parts[1]
    label = label_dict.get(category, None)
    if label is not None:
        image_labels.append((os.path.join(upload_folder, image_file), label))

# 拆分数据集为训练集和验证集
train_labels, val_labels = train_test_split(image_labels, test_size=0.2, random_state=42)

# 定义数据转换
train_transform = transforms.Compose([
    transforms.Resize(224),
    transforms.RandomHorizontalFlip(),
    transforms.RandomVerticalFlip(),
    transforms.RandomRotation(20),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

val_transform = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# 创建数据集和数据加载器
train_dataset = CustomImageDataset(train_labels, transform=train_transform)
val_dataset = CustomImageDataset(val_labels, transform=val_transform)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

# 初始化模型
num_classes = len(set(label_dict.values()))
model = EfficientNet.from_pretrained('efficientnet-b5')
num_ftrs = model._fc.in_features
model._fc = torch.nn.Linear(num_ftrs, num_classes)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

# 定义损失函数和优化器
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 定义学习率调度器
warmup_steps = 100  # 设置 Warmup 步数
total_steps = len(train_loader) * 10  # 总步数为 10 个 epoch
scheduler = WarmUpCosineDecayScheduler(
    optimizer,
    warmup_steps=warmup_steps,
    total_steps=total_steps,
    base_lr=0.001,
    final_lr=0.0001,
    warmup_lr=0.0
)

# 创建保存模型的目录
save_dir = 'checkpoints'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 训练和验证模型
num_epochs = 10

for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
        scheduler.step()  # 更新学习率
    
    model.eval()
    val_loss = 0.0
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in val_loader:
            images, labels = images.to(device), labels.to(device)
            
            outputs = model(images)
            loss = criterion(outputs, labels)
            val_loss += loss.item()
            
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    
    print(f"Epoch {epoch+1}/{num_epochs}, "
          f"Train Loss: {running_loss/len(train_loader):.4f}, "
          f"Val Loss: {val_loss/len(val_loader):.4f}, "
          f"Val Accuracy: {correct/total*100:.2f}%")
    
    # 保存模型
    torch.save({
        'epoch': epoch + 1,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'scheduler_state_dict': scheduler.state_dict(),
        'loss': running_loss / len(train_loader),
    }, os.path.join(save_dir, f'checkpoint_epoch_{epoch+1}.pth'))

# 保存最终模型
torch.save(model.state_dict(), os.path.join(save_dir, 'final_model.pth'))
