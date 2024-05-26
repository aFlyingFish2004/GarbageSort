import os
from sklearn.model_selection import train_test_split
import random

#该文件用于划分数据集

image_label_file = "image_labels.txt"
image_labels = []

with open(image_label_file, "r", encoding="utf-8") as f:
    for line in f:
        file_path, label = line.strip().split("\t")
        image_labels.append((file_path, label))

# 定义缩减比例，例如 1 表示使用全部数据
reduction_ratio = 1
reduced_image_labels = random.sample(
    image_labels, int(len(image_labels) * reduction_ratio)
)

# 拆分数据集为训练集和临时集
train_labels, temp_labels = train_test_split(
    reduced_image_labels, test_size=0.3, random_state=42
)

# 拆分临时集为验证集和测试集
val_labels, test_labels = train_test_split(
    temp_labels, test_size=0.5, random_state=42
)

# 将训练集写入 train.txt
with open("train.txt", "w", encoding="utf-8") as train_file:
    for file_path, label in train_labels:
        train_file.write(f"{file_path}\t{label}\n")

# 将验证集写入 val.txt
with open("val.txt", "w", encoding="utf-8") as val_file:
    for file_path, label in val_labels:
        val_file.write(f"{file_path}\t{label}\n")

# 将测试集写入 test.txt
with open("test.txt", "w", encoding="utf-8") as test_file:
    for file_path, label in test_labels:
        test_file.write(f"{file_path}\t{label}\n")

print("训练集、验证集和测试集已分别写入 train.txt、val.txt 和 test.txt 文件中")
