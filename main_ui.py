# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Coffee_Anytime_3/UI/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 391, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("data\\anytime.JPG"))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(400, 60, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 20, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_degree = QtWidgets.QLabel(self.centralwidget)
        self.label_degree.setGeometry(QtCore.QRect(10, 130, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_degree.setFont(font)
        self.label_degree.setObjectName("label_degree")
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(10, 190, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_status.setFont(font)
        self.label_status.setObjectName("label_status")
        self.label_taste = QtWidgets.QLabel(self.centralwidget)
        self.label_taste.setGeometry(QtCore.QRect(10, 220, 771, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_taste.setFont(font)
        self.label_taste.setObjectName("label_taste")
        self.label_volume = QtWidgets.QLabel(self.centralwidget)
        self.label_volume.setGeometry(QtCore.QRect(460, 130, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_volume.setFont(font)
        self.label_volume.setObjectName("label_volume")
        self.label_price = QtWidgets.QLabel(self.centralwidget)
        self.label_price.setGeometry(QtCore.QRect(460, 190, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_price.setFont(font)
        self.label_price.setObjectName("label_price")
        self.ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button.setGeometry(QtCore.QRect(730, 0, 60, 60))
        self.ok_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data\\mark.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ok_button.setIcon(icon)
        self.ok_button.setIconSize(QtCore.QSize(60, 60))
        self.ok_button.setObjectName("ok_button")
        self.change_but = QtWidgets.QPushButton(self.centralwidget)
        self.change_but.setGeometry(QtCore.QRect(330, 310, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.change_but.setFont(font)
        self.change_but.setObjectName("change_but")
        self.refresh_but = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_but.setGeometry(QtCore.QRect(670, 0, 60, 60))
        self.refresh_but.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("data\\fresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_but.setIcon(icon1)
        self.refresh_but.setIconSize(QtCore.QSize(60, 60))
        self.refresh_but.setObjectName("refresh_but")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Coffee Anytime"))
        self.label_2.setText(_translate("MainWindow", "????????..."))
        self.label_degree.setText(_translate("MainWindow", "?????????????? ??????????????:"))
        self.label_status.setText(_translate("MainWindow", "??????:"))
        self.label_taste.setText(_translate("MainWindow", "????????:"))
        self.label_volume.setText(_translate("MainWindow", "?????????? ??????????????:"))
        self.label_price.setText(_translate("MainWindow", "????????:"))
        self.change_but.setText(_translate("MainWindow", "????????????????"))
