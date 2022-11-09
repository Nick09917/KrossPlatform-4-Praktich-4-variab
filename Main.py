#!/usr/bin/env python3
# coding=utf-8

import sys
from datetime import time
from random import randint, random

from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('Работа с визуальными табличными данными в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_random_number.clicked.connect(self.fill_random)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random(self):
        """
        Метод для кнопки "Заполнить случайными числами"
        Случайные числа от 1 до 100
        """
        self.label_info.setText("")
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                random_num2 = random()*100
                random_num = round(random_num2,1)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))

    def solve(self):
        """
        Метод для кнопки "Выполнить задание"
        """
        result = find_max_min_sum(self.tableWidget)
        if result[7] == 0:
            self.label_info.setText("0 не найден в таблице!")
        else:
            self.label_info.setText("Ноль найден, все вещ элементы = 1")


            ff = result[7]



            if ff:
                print("0 yes")
                row = 0
                col = 0
                for row in range(self.tableWidget.rowCount()):
                    for col in range(self.tableWidget.columnCount()):
                        self.tableWidget.setItem(row, col, QTableWidgetItem("1"))

            else:
                print("0 no")


def find_max_min_sum(table_widget):
    """
    Поиск максимума, минимума и суммы в таблице
    :param table_widget: таблица
    :return: список с данными: max_num, row_max_number, col_max_number,
            min_num, row_min_number, col_min_number,
            sum_table
    """

    row_max_number = 0
    col_max_number = 0
    row_min_number = 0
    col_min_number = 0
    sum_table = 0
    max_num = float(table_widget.item(row_max_number, col_max_number).text())
    min_num = max_num

    ff = 0
    for row in range(table_widget.rowCount()):
        for col in range(table_widget.columnCount()):
            number = float(table_widget.item(row, col).text())
            if number >= max_num:
                max_num = number
                row_max_number = row
                col_max_number = col
            if number <= min_num:
                min_num = number
                row_min_number = row
                col_min_number = col
            sum_table = sum_table + number
            if number == 0:
                ff = 1


    return [max_num, row_max_number, col_max_number,
            min_num, row_min_number, col_min_number,
            sum_table, ff]


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
