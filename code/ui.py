# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dog_vs_Cat.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self,Dialog):
        self.Dialog = Dialog
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(730, 589)
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_4 = QtWidgets.QLabel(self.Dialog)

    def setupUi(self):
        self.label.setGeometry(QtCore.QRect(220, 130, 341, 331))
        self.label.setObjectName("label")

        self.label_2.setGeometry(QtCore.QRect(20, 10, 131, 81))
        self.label_2.setObjectName("label_2")

        self.pushButton.setGeometry(QtCore.QRect(570, 40, 111, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2.setGeometry(QtCore.QRect(570, 80, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_3.setGeometry(QtCore.QRect(220, 540, 71, 31))
        self.label_3.setObjectName("label_3")

        self.label_4.setGeometry(QtCore.QRect(300, 550, 54, 12))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "展示图片"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "选择要鉴别的图片"))
        self.pushButton_2.setText(_translate("Dialog", "开始鉴别"))
        self.label_3.setText(_translate("Dialog", "鉴别结果是："))
        self.label_4.setText(_translate("Dialog", ""))
