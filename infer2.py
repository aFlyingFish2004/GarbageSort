import os
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

# 设置使用的GPU设备
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


def softmax(x):
    exp_x = np.exp(x - np.max(x))  # 防止溢出
    softmax_x = exp_x / np.sum(exp_x)
    return softmax_x


# 读取标签文件
with open("dir_label.txt", "r", encoding="utf-8") as f:
    labels = f.readlines()
    labels = list(map(lambda x: x.strip().split("\t"), labels))
    labels_dict = {int(label[1]): label[0] for label in labels}


def padding_black(img):
    w, h = img.size
    scale = 224.0 / max(w, h)
    img_fg = img.resize([int(x) for x in [w * scale, h * scale]])

    size_fg = img_fg.size
    size_bg = 224

    img_bg = Image.new("RGB", (size_bg, size_bg))

    img_bg.paste(img_fg, ((size_bg - size_fg[0]) // 2, (size_bg - size_fg[1]) // 2))

    img = img_bg
    return img


# 加载图片并进行预处理
def load_image(image_path, train_flag=True):
    transform_train = transforms.Compose(
        [
            transforms.Resize(224),
            transforms.RandomHorizontalFlip(),
            transforms.RandomVerticalFlip(),
            transforms.ToTensor(),
        ]
    )

    transform_val = transforms.Compose(
        [
            transforms.Resize(224),
            transforms.ToTensor(),
        ]
    )

    img = Image.open(image_path).convert("RGB")
    img = padding_black(img)
    if train_flag:
        img = transform_train(img)
    else:
        img = transform_val(img)

    img = img.unsqueeze(0)  # 增加一个批次维度
    return img


# 预测函数
def predict(image_path):
    # 加载模型
    weights = models.ResNet50_Weights.DEFAULT
    model = models.resnet50(weights=weights)
    fc_inputs = model.fc.in_features
    model.fc = nn.Linear(fc_inputs, 214)
    model = model.cuda()

    # 加载训练好的模型
    checkpoint = torch.load("model_best_checkpoint_resnet50.pth.tar")
    model.load_state_dict(checkpoint["state_dict"])
    model.eval()

    # 加载图片
    image = load_image(image_path, train_flag=False)  # 对单张图片进行验证处理
    image = image.cuda()

    # 进行预测
    with torch.no_grad():  # 不需要计算梯度
        pred = model(image)

    pred = pred.cpu().numpy()[0]
    score = softmax(pred)
    pred_id = np.argmax(score)

    # 显示结果
    img = Image.open(image_path).convert("RGB")
    img = padding_black(img)
    print(f"预测结果: {labels_dict[pred_id]}")


if __name__ == "__main__":
    image_path = "可回收物_水杯/可回收物_水杯_2.jpg"  # 替换为你要预测的图片路径
    predict(image_path)
