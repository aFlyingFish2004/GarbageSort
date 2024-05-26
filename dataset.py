import os
import torch
from torch.utils.data import Dataset, DataLoader
from PIL import Image
from torchvision import transforms

# 假设您的标签文档是一个纯文本文件
label_file = "label.txt"

# 创建一个字典，将类别映射到标签
label_dict = {}
with open(label_file, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("\t")
        pre = parts[0].strip().split("_")
        category = pre[1]  # 类别
        label = int(parts[1])  # 标签
        label_dict[category] = label
# 指定上传文件夹路径
upload_folder = "upload"

# 获取所有图片文件
image_files = [f for f in os.listdir(upload_folder) if f.endswith(".jpeg")]

# 提取文件名中的类别信息并生成标签
image_labels = []
t = 0
for image_file in image_files:
    # 文件名格式假设为 "img_类别_顺序编号.jpeg"
    parts = image_file.split("_")
    category = parts[1]  # 提取类别部分
    label = label_dict.get(category, None)  # 获取标签
    if label is not None:
        image_labels.append((os.path.join(upload_folder, image_file), label))


class CustomImageDataset(Dataset):
    def __init__(self, image_labels, transform=None):
        self.image_labels = image_labels
        self.transform = transform

    def __len__(self):
        return len(self.image_labels)

    def __getitem__(self, idx):
        img_path, label = self.image_labels[idx]
        image = Image.open(img_path).convert("RGB")
        image = self.padding_black(image)
        if self.transform:
            image = self.transform(image)
        return image, label

    def padding_black(self, img):
        w, h = img.size
        scale = 224.0 / max(w, h)
        img_fg = img.resize([int(x) for x in [w * scale, h * scale]])
        size_fg = img_fg.size
        size_bg = 224
        img_bg = Image.new("RGB", (size_bg, size_bg))
        img_bg.paste(img_fg, ((size_bg - size_fg[0]) // 2, (size_bg - size_fg[1]) // 2))
        img = img_bg
        return img


# 示例用法
if __name__ == "__main__":
    # 如果需要，可以在这里定义数据增强
    transform = transforms.Compose(
        [
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )
