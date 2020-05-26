from torch import nn
from torchvision import transforms, models
from torch.autograd import Variable
import torch
from PIL import Image
import os

rootPath = './testImg'
imgList = os.listdir(rootPath)
data_tf = transforms.Compose([
            transforms.Resize((64,64)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[.5,.5,.5],std=[.5,.5,.5])
        ])
DCModel = models.resnet18(pretrained=False)
dim_in = DCModel.fc.in_features
DCModel.fc = nn.Linear(dim_in,2)
DCModel.load_state_dict(torch.load('models/myModel.pth'))
DCModel.eval()
for item in imgList:
    imgPath = rootPath+'/'+item
    content = Image.open(imgPath)
    img = data_tf(content)
    img = torch.unsqueeze(img, 0)
    out = DCModel(img)
    _, pred = torch.max(out, 1)
    print(pred)


