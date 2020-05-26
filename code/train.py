from torch.autograd import Variable
from torchvision import models,datasets,transforms
import torch
from torch import nn,optim
from torch.utils.data import DataLoader
import argparse

parser = argparse.ArgumentParser(description='for DogVSCat')
parser.add_argument('-e','--epoch',help='',type=int,default=50)
parser.add_argument('-b','--batchSize',help='',type=int,default=1000)
parser.add_argument('-n','--num_classes',help='',type=int,default=2)
argvs = parser.parse_args()


DCModel = models.resnet18(pretrained=False)
DCModel.load_state_dict(torch.load("models/resnet18-5c106cde.pth"))
dim_in = DCModel.fc.in_features
DCModel.fc = nn.Linear(dim_in,argvs.num_classes)

data_tf = transforms.Compose([
            transforms.Resize((64,64)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[.5,.5,.5],std=[.5,.5,.5])
        ])
trainSet = datasets.ImageFolder('../dataset/train',transform=data_tf)
testSet = datasets.ImageFolder('../dataset/test',transform=data_tf)


train_loader = DataLoader(trainSet, batch_size=argvs.batchSize, shuffle=True)
test_loader = DataLoader(testSet,batch_size=argvs.batchSize, shuffle=True)

DCModel.cuda()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(DCModel.parameters(),lr=1e-3,momentum=0.5)
 
for epoch in range(argvs.epoch):
    DCModel.train()
    print("epoch:{}".format(epoch))
    trainLoss = 0
    train_acc = 0
    test_acc = 0
    train_label = 0
    test_label = 0 
    for data in train_loader:
        img, label = data
        print(img.size())
        img = Variable(img).cuda()
        label = Variable(label).cuda()
        out = DCModel(img)
        loss = criterion(out, label)
        trainLoss += loss.item()
        train_label += img.size(0)
        #print("loss:{}".format(loss.item() ))
       # print("label size:{}".format(label.size(0)))
        _, pred = torch.max(out, 1)
        num_acc = (pred == label).sum()
        print("train acc:{}".format(num_acc.item()/img.size(0)))
        train_acc += num_acc.item()
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print("train loss:{}".format(trainLoss))
    print("train acc:{}".format(train_acc/train_label))
    DCModel.eval()
    for data in test_loader:
        img, label = data
        img = Variable(img,requires_grad=False).cuda()
        label = Variable(label,requires_grad=False).cuda()
        out = DCModel(img)
        loss = criterion(out, label)
        _, pred = torch.max(out, 1)
        num_acc = (pred == label).sum()
        test_acc += num_acc.item()
        test_label += label.size(0)
        #print("test acc:{}".format(num_acc.item() / img.size(0)))
    print('test acc:{}'.format(test_acc/test_label))
torch.save(DCModel.state_dict(),'myModel.pth')