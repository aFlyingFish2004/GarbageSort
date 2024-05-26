#验证代码

import os
import torch
from torchvision import transforms
from torch.utils.data import DataLoader
from efficientnet_pytorch import EfficientNet
from dataload import CustomImageDataset  # 从 dataload.py 导入 CustomImageDataset
from tqdm import tqdm

# 定义数据转换
val_transform = transforms.Compose(
    [
        transforms.Resize((224, 224)),  # 调整图像尺寸为 224x224
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)


# 加载标签文件
def load_labels(label_file):
    label_map = {}
    with open(label_file, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            class_name = parts[0]
            class_index = int(parts[1])
            label_map[class_index] = class_name
    return label_map


# 加载模型
def load_model(model_path, num_classes):
    model = EfficientNet.from_name("efficientnet-b5")
    num_ftrs = model._fc.in_features
    model._fc = torch.nn.Linear(num_ftrs, num_classes)
    model.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")))
    model.eval()  # 设置为评估模式
    return model


# 验证函数
def validate(model, val_loader, device):
    model.eval()
    val_loss = 0.0
    correct = 0
    total = 0
    criterion = torch.nn.CrossEntropyLoss()

    val_loader = tqdm(val_loader, desc="Validation")
    with torch.no_grad():
        for images, labels in val_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)
            val_loss += loss.item()

            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    avg_val_loss = val_loss / len(val_loader)
    val_accuracy = correct / total * 100
    print(
        f"Validation Loss: {avg_val_loss:.4f}, Validation Accuracy: {val_accuracy:.2f}%"
    )
    return avg_val_loss, val_accuracy


if __name__ == "__main__":
    model_path = "checkpoints/final_model.pth"  # 替换为训练好的模型路径
    label_file = "label.txt"  # 标签文件路径
    val_data_file = "test.txt"  # 验证集文件路径
    num_classes = 214  # 类别数量
    batch_size = 64  # 批次大小
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    label_map = load_labels(label_file)
    val_dataset = CustomImageDataset(label_file=val_data_file, transform=val_transform)
    val_loader = DataLoader(
        val_dataset, batch_size=batch_size, shuffle=False, num_workers=4
    )

    model = load_model(model_path, num_classes)
    model = model.to(device)

    validate(model, val_loader, device)
