# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Coffee_Anytime_3/UI/addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 370)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 50, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cb_choose = QtWidgets.QComboBox(Form)
        self.cb_choose.setGeometry(QtCore.QRect(100, 50, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.cb_choose.setFont(font)
        self.cb_choose.setObjectName("cb_choose")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 250, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 280, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line_v = QtWidgets.QLineEdit(Form)
        self.line_v.setGeometry(QtCore.QRect(120, 220, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.line_v.setFont(font)
        self.line_v.setObjectName("line_v")
        self.line_price = QtWidgets.QLineEdit(Form)
        self.line_price.setGeometry(QtCore.QRect(120, 250, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.line_price.setFont(font)
        self.line_price.setObjectName("line_price")
        self.ok_but = QtWidgets.QPushButton(Form)
        self.ok_but.setGeometry(QtCore.QRect(10, 320, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ok_but.setFont(font)
        self.ok_but.setObjectName("ok_but")
        self.mark_but = QtWidgets.QPushButton(Form)
        self.mark_but.setGeometry(QtCore.QRect(350, 50, 41, 41))
        self.mark_but.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/mark.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mark_but.setIcon(icon)
        self.mark_but.setIconSize(QtCore.QSize(41, 41))
        self.mark_but.setObjectName("mark_but")
        self.status_bar = QtWidgets.QLabel(Form)
        self.status_bar.setGeometry(QtCore.QRect(0, 350, 391, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.status_bar.setFont(font)
        self.status_bar.setText("")
        self.status_bar.setObjectName("status_bar")
        self.cb_status = QtWidgets.QComboBox(Form)
        self.cb_status.setGeometry(QtCore.QRect(120, 190, 271, 22))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.cb_status.setFont(font)
        self.cb_status.setObjectName("cb_status")
        self.cb_degree = QtWidgets.QComboBox(Form)
        self.cb_degree.setGeometry(QtCore.QRect(120, 160, 271, 22))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.cb_degree.setFont(font)
        self.cb_degree.setObjectName("cb_degree")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 33))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_but = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.add_but.setFont(font)
        self.add_but.setObjectName("add_but")
        self.button_group = QtWidgets.QButtonGroup(Form)
        self.button_group.setObjectName("button_group")
        self.button_group.addButton(self.add_but)
        self.horizontalLayout.addWidget(self.add_but)
        self.edit_but = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.edit_but.setFont(font)
        self.edit_but.setObjectName("edit_but")
        self.button_group.addButton(self.edit_but)
        self.horizontalLayout.addWidget(self.edit_but)
        self.del_but = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.del_but.setFont(font)
        self.del_but.setObjectName("del_but")
        self.button_group.addButton(self.del_but)
        self.horizontalLayout.addWidget(self.del_but)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 110, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.name_line = QtWidgets.QLineEdit(Form)
        self.name_line.setGeometry(QtCore.QRect(120, 110, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.name_line.setFont(font)
        self.name_line.setObjectName("name_line")
        self.line_taste = QtWidgets.QTextEdit(Form)
        self.line_taste.setGeometry(QtCore.QRect(120, 280, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.line_taste.setFont(font)
        self.line_taste.setObjectName("line_taste")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "?????????????????? ????????????"))
        self.label.setText(_translate("Form", "??????????????:"))
        self.label_2.setText(_translate("Form", "????.??????????????"))
        self.label_3.setText(_translate("Form", "??????"))
        self.label_4.setText(_translate("Form", "??????????"))
        self.label_5.setText(_translate("Form", "????????"))
        self.label_6.setText(_translate("Form", "????????"))
        self.ok_but.setText(_translate("Form", "????"))
        self.add_but.setText(_translate("Form", "????????????????"))
        self.edit_but.setText(_translate("Form", "????????????????"))
        self.del_but.setText(_translate("Form", "??????????????"))
        self.label_7.setText(_translate("Form", "????????????????"))
