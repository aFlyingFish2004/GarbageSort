import torch
from efficientnet_pytorch import EfficientNet


def initialize_model(num_classes, use_pretrained=True):
    model = EfficientNet.from_pretrained("efficientnet-b5")
    num_ftrs = model._fc.in_features
    model._fc = torch.nn.Linear(num_ftrs, num_classes)
    return model



