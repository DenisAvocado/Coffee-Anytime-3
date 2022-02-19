import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QWidget
from main_ui import Ui_MainWindow
from addEditCoffeeForm_ui import Ui_Form


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
        # uic.loadUi("UI/addEditCoffeeForm.ui", self)
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