import os
from PIL import Image, ImageFile
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms

ImageFile.LOAD_TRUNCATED_IMAGES = True  # 处理截断的图像文件

# 自定义 Dataset 类
class CustomImageDataset(Dataset):
    def __init__(self, label_file, transform=None):
        self.image_labels = []
        with open(label_file, "r", encoding="utf-8") as f:
            for line in f:
                file_path, label = line.strip().split("\t")
                self.image_labels.append((file_path, int(label)))
        self.transform = transform

    def __len__(self):
        return len(self.image_labels)

    def __getitem__(self, idx):
        img_path, label = self.image_labels[idx]
        try:
            image = Image.open(img_path).convert("RGB")
        except Exception as e:
            print(f"Error loading image {img_path}: {e}")
            return None, None

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

# 定义图像转换
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
])

# 使用 DataLoader 加载数据
train_dataset = CustomImageDataset(label_file="train.txt", transform=transform)
val_dataset = CustomImageDataset(label_file="val.txt", transform=transform)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, num_workers=4)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False, num_workers=4)

# 检查 DataLoader 是否正常工作
for images, labels in train_loader:
    if images is None or labels is None:
        continue  # 跳过加载失败的样本
    print(images.shape, labels.shape)  # 打印图像和标签的形状
    break
