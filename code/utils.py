import torch
from torch import nn
from torchvision import models


class DCModel:
    def __init__(self):
        self.savePath = 'models/myModel.pth'

    def get_eval_model(self):
        DCModel = models.resnet18(pretrained=False)
        dim_in = DCModel.fc.in_features
        DCModel.fc = nn.Linear(dim_in, 2)
        DCModel.load_state_dict(torch.load(self.savePath))
        return DCModel.eval()