import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QWidget
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
        self.label_2.setText(_translate("MainWindow", "Кофе..."))
        self.label_degree.setText(_translate("MainWindow", "Степень обжарки:"))
        self.label_status.setText(_translate("MainWindow", "Вид:"))
        self.label_taste.setText(_translate("MainWindow", "Вкус:"))
        self.label_volume.setText(_translate("MainWindow", "Объем стакана:"))
        self.label_price.setText(_translate("MainWindow", "Цена:"))
        self.change_but.setText(_translate("MainWindow", "Изменить"))


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
        Form.setWindowTitle(_translate("Form", "Изменение данных"))
        self.label.setText(_translate("Form", "Выбрать:"))
        self.label_2.setText(_translate("Form", "Ст.обжарки"))
        self.label_3.setText(_translate("Form", "Вид"))
        self.label_4.setText(_translate("Form", "Объем"))
        self.label_5.setText(_translate("Form", "Цена"))
        self.label_6.setText(_translate("Form", "Вкус"))
        self.ok_but.setText(_translate("Form", "ОК"))
        self.add_but.setText(_translate("Form", "Добавить"))
        self.edit_but.setText(_translate("Form", "Изменить"))
        self.del_but.setText(_translate("Form", "Удалить"))
        self.label_7.setText(_translate("Form", "Название"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("data/coffee.sqlite")
        self.cur = self.con.cursor()
        self.ok_button.clicked.connect(self.ok)
        self.change_but.clicked.connect(self.change)
        self.refresh_but.clicked.connect(self.fill_combobox)
        self.fill_combobox()

    def ok(self):
        self.label_degree.setText('Степень обжарки:')
        self.label_status.setText('Вид:')
        self.label_taste.setText('Вкус:')
        self.label_price.setText('Цена:')
        self.label_volume.setText('Объем стакана:')
        command = '''SELECT * FROM coffie_variants WHERE sort_name = ?'''
        res = self.cur.execute(command, (self.comboBox.currentText(),)).fetchone()
        degree = self.cur.execute(f'''SELECT degree FROM degree_of_roasting WHERE
         id = {res[2]}''').fetchone()
        status = self.cur.execute(f'''SELECT status_name FROM status WHERE
         id = {res[3]}''').fetchone()
        self.label_degree.setText(f'{self.label_degree.text()} {degree[0]}')
        self.label_status.setText(f'{self.label_status.text()} {status[0]}')
        self.label_taste.setText(f'{self.label_taste.text()} {res[4]}')
        self.label_price.setText(f'{self.label_price.text()} {res[5]} руб.')
        self.label_volume.setText(f'{self.label_volume.text()} {res[6]} мл')

    def fill_combobox(self):
        self.comboBox.clear()
        command = '''SELECT sort_name FROM coffie_variants'''
        res = self.cur.execute(command).fetchall()
        lst = [elem[0] for elem in res]
        self.comboBox.addItems(lst)

    def change(self):
        self.second_form = ChangeWidget()
        self.second_form.show()


class ChangeWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("data/coffee.sqlite")
        self.cur = self.con.cursor()
        self.mark_but.clicked.connect(self.upload)
        self.ok_but.clicked.connect(self.ok)
        self.fill_combobox()
        self.last_operator = None
        self.add_but.clicked.connect(self.get_last_operator)
        self.del_but.clicked.connect(self.get_last_operator)
        self.edit_but.clicked.connect(self.get_last_operator)

    def fill_combobox(self):
        self.cb_degree.clear()
        self.cb_status.clear()
        self.cb_choose.clear()
        command = '''SELECT degree FROM degree_of_roasting'''
        lst = [elem[0] for elem in self.cur.execute(command).fetchall()]
        self.cb_degree.addItems(lst)
        command = '''SELECT status_name FROM status'''
        lst = [elem[0] for elem in self.cur.execute(command).fetchall()]
        self.cb_status.addItems(lst)
        command = '''SELECT sort_name FROM coffie_variants'''
        lst = [elem[0] for elem in self.cur.execute(command).fetchall()]
        self.cb_choose.addItems(lst)
        return lst

    def upload(self):
        command = '''SELECT * FROM coffie_variants WHERE sort_name = ?'''
        res = self.cur.execute(command, (self.cb_choose.currentText(),)).fetchone()
        degree = self.cur.execute(f'''SELECT degree FROM degree_of_roasting WHERE
                 id = {res[2]}''').fetchone()[0]
        status = self.cur.execute(f'''SELECT status_name FROM status WHERE
                 id = {res[3]}''').fetchone()[0]
        self.cb_degree.setCurrentText(degree)
        self.cb_status.setCurrentText(status)
        self.line_v.setText(str(res[6]))
        self.line_price.setText(str(res[5]))
        self.line_taste.setText(res[4])
        self.name_line.setText(res[1])

    def ok(self):
        self.get_last_operator()
        if self.last_operator == 'Добавить':
            if self.cb_degree.currentText() == '' or self.cb_status.currentText() == '' \
                    or self.line_v.text() == '' or self.line_price.text() == '':
                self.status_bar.setText('Не все поля заполнены!')
                return
            else:
                command = '''SELECT id FROM degree_of_roasting WHERE degree = ?'''
                deg_id = self.cur.execute(command, (self.cb_degree.currentText(),)).fetchone()[0]
                command = '''SELECT id FROM status WHERE status_name = ?'''
                st_id = self.cur.execute(command, (self.cb_status.currentText(),)).fetchone()[0]
                command = '''INSERT INTO coffie_variants(sort_name, degree_id,
                 status_id, taste, price, packet_v) VALUES(?, ?, ?, ?, ?, ?)'''
                self.cur.execute(command, (self.name_line.text(), deg_id, st_id,
                                           self.line_taste.toPlainText(), self.line_price.text(),
                                           self.line_v.text()))
                self.fill_combobox()
                self.status_bar.setText('Успешно добавлено!')
        elif self.last_operator == 'Удалить':
            if self.cb_degree.currentText() == '' or self.cb_status.currentText() == '' \
                    or self.line_v.text() == '' or self.line_price.text() == '':
                self.status_bar.setText('Вы не выбрали, что удалять!')
                return
            else:
                if self.name_line.text() in self.fill_combobox():
                    command = '''DELETE FROM coffie_variants WHERE sort_name = ?'''
                    self.cur.execute(command, (self.name_line.text(),))
                    self.status_bar.setText('Удалено!')
                else:
                    self.status_bar.setText('Такой записи нет')
                    return
        elif self.last_operator == 'Изменить':
            if self.cb_degree.currentText() == '' or self.cb_status.currentText() == '' \
                    or self.line_v.text() == '' or self.line_price.text() == '':
                self.status_bar.setText('Вы не выбрали, что изменять!')
                return
            else:
                command = '''SELECT id FROM coffie_variants WHERE sort_name = ?'''
                res = self.cur.execute(command, (self.cb_choose.currentText(),)).fetchone()
                cof_id = res[0]
                command = '''SELECT id FROM degree_of_roasting WHERE degree = ?'''
                deg_id = self.cur.execute(command, (self.cb_degree.currentText(),)).fetchone()[0]
                command = '''SELECT id FROM status WHERE status_name = ?'''
                st_id = self.cur.execute(command, (self.cb_status.currentText(),)).fetchone()[0]
                command = '''UPDATE coffie_variants
                 SET
                 sort_name = ?,
                 degree_id = ?,
                 status_id = ?,
                 taste = ?,
                 price = ?,
                 packet_v = ?
                 WHERE id = ?'''
                self.cur.execute(command, (self.name_line.text(), deg_id, st_id,
                                       self.line_taste.toPlainText(), self.line_price.text(),
                                       self.line_v.text(), cof_id,))
                self.status_bar.setText('Изменено!')
        self.con.commit()

    def get_last_operator(self):
        if self.sender().text() in ['Добавить', 'Изменить', 'Удалить']:
            self.last_operator = self.sender().text()
            self.status_bar.setText(f'Что Вы хотите {self.last_operator.lower()}?')
            return self.last_operator


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())