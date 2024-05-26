# 带前三相似度显示的预测代码


import os
import torch
from torchvision import transforms
from PIL import Image
from efficientnet_pytorch import EfficientNet



# 定义数据转换
inference_transform = transforms.Compose(
    [
        transforms.Resize((224, 224)),
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
def infer(model, image_path, label_map):
    image = Image.open(image_path).convert("RGB")
    image = inference_transform(image)
    image = image.unsqueeze(0)  # 增加批次维度

    with torch.no_grad():
        output = model(image)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)  # 计算概率
        top3_prob, top3_catid = torch.topk(probabilities, 3)  # 获取前3个类别及其概率

    results = [
        (label_map[catid.item()], prob.item())
        for catid, prob in zip(top3_catid, top3_prob)
    ]
    return results


def infer_image(model, folder_path, image_name, label_map):
    image_path = os.path.join(folder_path, image_name)
    if os.path.exists(image_path) and image_name.endswith(("jpeg", "jpg", "png")):
        prediction = infer(model, image_path, label_map)
        print(f"Image: {image_path}")
        res_list = []
        for label, prob in prediction:
            print(f"  Predicted class: {label}, Similarity: {prob:.4f}")
            res_list.append((label, format(float(format(prob, ".4f")), '.00%')))
        return res_list
    else:
        print(f"Image {image_name} not found in folder {folder_path} or unsupported file type.")
        return None


def predict(image_name):
    # model_path = "checkpoints/final_model.pth"  # 模型路径
    model_path = os.path.join(os.path.dirname(__file__), "checkpoints/final_model.pth")
    label_file = os.path.join(os.path.dirname(__file__), "label.txt")  # 标签文件路径
    # 动态构建与 infer2 同级的 images 文件夹路径
    folder_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "images")
    num_classes = 214  # 类别数量

    model = load_model(model_path, num_classes)
    label_map = load_labels(label_file)
    res = infer_image(model, folder_path, image_name, label_map)
    top1_res = res[0][0]
    top2_res = res[1][0]
    top3_res = res[2][0]
    top1_pro = res[0][1]
    top2_pro = res[1][1]
    top3_pro = res[2][1]
    return top1_pro, top2_pro, top3_pro, top1_res, top2_res, top3_res


if __name__ == "__main__":
    print(predict('2_ph.jpg'))
