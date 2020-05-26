import sys

import torch
from PIL import Image
from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5 import QtGui
from qtpy import QtWidgets
from torchvision import transforms

from ui import Ui_Dialog
from utils import DCModel

class DC(Ui_Dialog):
    def __init__(self,Form):
        super(DC, self).__init__(Form)
        model = DCModel()
        self.model = model.get_eval_model()
        self.data_tf = transforms.Compose([
            transforms.Resize((64, 64)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[.5, .5, .5], std=[.5, .5, .5])
        ])
        self.imgPath = ''
        self.pushButton.clicked.connect(self.getPicture)
        self.pushButton_2.clicked.connect(self.predict)

    def predict(self):
        try:
            content = Image.open(self.imgPath)
            img = self.data_tf(content)
            img = torch.unsqueeze(img, 0)
            out = self.model(img)
            _, pred = torch.max(out, 1)
            if pred.item() == 0:
                print('猫')
                self.label_4.setText('猫')
            else:
                print('狗')
                self.label_4.setText('狗')
        except Exception as e:
            print(e)

    def getPicture(self):
        print('chose Picture')
        try:
            fileName,_ = QFileDialog.getOpenFileName(self.Dialog, "Open File",
                                                   "./testImg",
                                                   "Images (*.png *.xpm *.jpg)")
            self.imgPath = fileName
        except Exception as e:
            print(e)
        print(self.imgPath)
        jpg = QtGui.QPixmap(self.imgPath).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)
        # imgName, imgType = QFileDialog.getOpenFileName(self, "打开您需要鉴定的图片", "", "*.jpg;;*.png;;All Files(*)")
        # jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        # self.label.setPixmap(jpg)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = DC(MainWindow)
    ui.setupUi()
    MainWindow.show()
    sys.exit(app.exec_())