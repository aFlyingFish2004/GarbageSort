
# 不带前三相似度显示的预测代码
import os
import torch
from torchvision import transforms
from PIL import Image
from efficientnet_pytorch import EfficientNet

# 定义数据转换
inference_transform = transforms.Compose(
    [
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)


# 加载训练好的模型
def load_model(model_path, num_classes):
    model = EfficientNet.from_name("efficientnet-b5")
    num_ftrs = model._fc.in_features
    model._fc = torch.nn.Linear(num_ftrs, num_classes)
    model.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")))
    model.eval()  # 设置为评估模式
    return model


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


# 推理函数
def infer(model, image_path):
    image = Image.open(image_path).convert("RGB")
    image = inference_transform(image)
    image = image.unsqueeze(0)  # 增加批次维度

    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)

    return predicted.item()


# 遍历文件夹并进行推理
def infer_folder(model, folder_path, label_map):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(("jpeg", "jpg", "png")):  # 支持的文件类型
                image_path = os.path.join(root, file)
                prediction = infer(model, image_path)
                class_name = label_map.get(prediction, "Unknown")
                print(f"Image: {image_path}, Predicted class: {class_name}")


if __name__ == "__main__":
    model_path = "checkpoints/final_model.pth"  # 模型路径
    label_file = "label.txt"  # 标签文件路径
    num_classes = 214  # 类别数量
    folder_path = "upload"  # 替换为你的文件夹路径

    model = load_model(model_path, num_classes)
    label_map = load_labels(label_file)
    infer_folder(model, folder_path, label_map)
