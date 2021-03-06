# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import threading

from PyQt5.QtCore import Qt
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import requests
from PyQt5.QtGui import QBrush, QFont
from PyQt5.QtWidgets import QTableView
from device_bitable import DeviceBitable
import time
from log import Ui_Form


# Thread trả về toàn bộ dữ liệu trong file Scorc.json

class MyThread(QThread):
    change_value = pyqtSignal(str)

    def run(self):
        result = dict()
        while True:

            dir = "./logs/"
            l = os.listdir(dir)
            ll = [i for i in l if len(i.split("_")) >= 3]
            for i in ll:
                File = open("./logs/" + i, "r")
                score_data = File.read()
                File.close()
                if score_data != "":
                    score_data = json.loads(score_data)
                    result.update(score_data)

                # score_data = '{"BITABLE_600": {"Wifi": [24, 0, 24], "LAN": [22, 2, 24], "bluetooth": [0, 12, 12]}}'
                # k = open("./logs/Score.json", "w")
                # k.write(score_data)
                # k.close()

            time.sleep(1)
            self.change_value.emit(json.dumps(result))


# Model chính của tableView Qt5
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        if role == Qt.BackgroundRole:
            if self._data[index.row()][11] == "1":
                return QBrush(Qt.green)
            else:
                return QBrush(Qt.white)



    def set_data_col_row(self, row_index, column_index, val, val1, val2):
        self._data[row_index][column_index] = str(val) + "/" + str(val2)
        self._data[row_index][column_index + 1] = str(val1) + "/" + str(val2)

    def data_col_row(self, row_index, col_index):
        return self._data[row_index][col_index]

    def data_row(self, row_index):
        return self._data[row_index]

    def data_row_color(self, row_index):
        # if role == Qt.BackgroundRole:
        return QBrush(Qt.green)

    def getAllData(self):
        return self._data

    def changeStatus(self, row_index, status):
        if status == True:
            self._data[row_index][11] = "1"
        else:
            self._data[row_index][11] = "0"

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class file:

    def __init__(self):
        self.a = 1


# a = file().a
# b = file().a

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        # --------------- IU ------------------
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1167, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(20, 20, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.add_device = QtWidgets.QPushButton(self.centralwidget)
        self.add_device.setGeometry(QtCore.QRect(200, 20, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.add_device.setFont(font)
        self.add_device.setObjectName("add_device")

        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(280, 510, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_start.setFont(font)
        self.btn_start.setObjectName("start_test")
        self.list_device = QtWidgets.QTableView(self.centralwidget)
        self.list_device.setGeometry(QtCore.QRect(20, 150, 1131, 351))
        self.list_device.setObjectName("list_device")
        self.token = QtWidgets.QTextEdit(self.centralwidget)
        self.token.setGeometry(QtCore.QRect(20, 80, 1131, 61))
        self.token.setObjectName("token")

        self.btn_startall = QtWidgets.QPushButton(self.centralwidget)
        self.btn_startall.setGeometry(QtCore.QRect(20, 510, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_startall.setFont(font)
        self.btn_startall.setObjectName("btn_stop")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(550, 510, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stop.setFont(font)
        self.btn_stop.setObjectName("start_test_3")
        self.btn_stopall = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stopall.setGeometry(QtCore.QRect(850, 510, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stopall.setFont(font)
        self.btn_stopall.setObjectName("start_test_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ------------ My change -------------------
        self.susscessorfailed = MyThread()
        self.thr = None
        self.data = [
            ["NAME", "BLUETOOTH NAME", "IP LAN", "IP WIFI", "BT SUCCESS", "BT FAILED", "LAN SUCCESS", "LAN FAILED",
             "WIFI SUCCESS", "WIFI FAILED", "LOG", "IS ENABLE"]
        ]

        self.threads = {}
        self.currentRow = None
        self.model = TableModel(self.data)
        self.list_device.setModel(self.model)
        # self.list_device.setCo
        self.list_device.setColumnWidth(11, 0)
        self.name.setText("BITABLE_")
        self.event()
        self.login()

    def login(self):
        response = requests.post('http://api.cms.beetai.com/api/user/login',
                                 json={'email': 'admin@beetsoft.com.vn', "password": "beetai@2019"})
        res = json.loads(response.text)
        self.token.setText(res['access_token'])
        self.token.setEnabled(False)

    def in_array(self, name_device):
        for item in self.data:
            if name_device == item[0]:
                return True
        return False

    def call_api(self, name_device):
        try:
            respose = requests.get("http://api.bitableconnect.beetai.com/get-ip-box?id=" + name_device)
            data_json = json.loads(respose.text)
            return data_json['lan'], data_json['wifi']
        except:
            return None, None

    def add_device_to_list(self, device):

        if device in self.threads:
            print("Device in threads")
            return
        else:
            self.threads[device] = None
        device = device.upper()
        lan, wifi = self.call_api(device)
        if lan != None:
            print(self.call_api(device))
            self.data.append([device, device, lan, wifi, "0/0", "0/0", "0/0", "0/0", "0/0", "0/0", "SHOW", "0"])
            self.model = TableModel(self.data)
            self.list_device.setModel(self.model)

            self.susscessorfailed.change_value.connect(self.process)
            self.susscessorfailed.start()
        self.name.setText("BITABLE_")

    def process(self, val):
        # print(val)
        if val != "":
            Data = json.loads(val)
            position = 0
            for i in self.data[1:]:
                position += 1
                if i[0] in Data:
                    self.model.set_data_col_row(row_index=position, column_index=4, val=Data[i[0]]["bluetooth"][0],
                                                val1=Data[i[0]]["bluetooth"][1],
                                                val2=Data[i[0]]["bluetooth"][2])
                    self.model.set_data_col_row(row_index=position, column_index=6, val=Data[i[0]]["LAN"][0],
                                                val1=Data[i[0]]["LAN"][1],
                                                val2=Data[i[0]]["LAN"][2])
                    self.model.set_data_col_row(row_index=position, column_index=8, val=Data[i[0]]["Wifi"][0],
                                                val1=Data[i[0]]["Wifi"][1],
                                                val2=Data[i[0]]["Wifi"][2])
            self.list_device.setModel(self.model)

        pass

    def event(self):
        self.list_device.clicked.connect(self.func_test)
        self.add_device.clicked.connect(self.add_new)
        self.btn_start.clicked.connect(self.handle_start)
        self.list_device.clicked.connect(self.tableView_log_row_onclick)
        self.list_device.setSelectionBehavior(QTableView.SelectRows)
        self.btn_startall.clicked.connect(self.handle_startall)
        self.btn_stop.clicked.connect(self.handle_stop)
        self.btn_stopall.clicked.connect(self.handle_stopall)

    def handle_startall(self):
        token = self.token.toPlainText()
        if len(token) == 0:
            print("missing token !!!")
            return
        if len(self.data) <= 1:
            return

        data_row = self.model.getAllData()
        # if data_row[0] not in self.threads:
        count = 1
        for i in data_row[1:]:
            # print(i[0])
            if i[0] in self.threads and self.threads[i[0]] is None:
                self.threads[i[0]] = DeviceBitable(i, self.token.toPlainText())
                # a = thread_with_trace(target=d.run, args=())
                self.threads[i[0]].status = 1
                self.threads[i[0]].start()
                # t = threading.Thread(target=d.run, args=())

                # self.btn_start.setEnabled(False)
                # self.btn_stop.setEnabled(True)
                self.model.data_row_color(count)
                self.model.changeStatus(count, True)

            elif i[0] in self.threads and self.threads[i[0]] is not None:
                self.threads[i[0]].continues()
                self.btn_start.setEnabled(False)
                self.btn_stop.setEnabled(True)
                self.model.data_row_color(count)
                self.model.changeStatus(count, True)

            count += 1

    def openLogWindow(self, item):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window, item.model().data_col_row(item.row(), 1))

        self.window.show()

    def tableView_log_row_onclick(self, item):
        if item.row() == 0:
            self.btn_start.setEnabled(False)
            return

        self.currentRow = item
        data_row = self.model.data_row(self.currentRow.row())
        try:
            if data_row[0] in self.threads and self.threads[data_row[0]].status == 1:
                self.btn_start.setEnabled(False)
                self.btn_stop.setEnabled(True)

            else:
                self.btn_start.setEnabled(True)
                self.btn_stop.setEnabled(False)
        except:
            self.btn_start.setEnabled(True)
            self.btn_stop.setEnabled(False)

        if item.column() != 10:
            return
        # print("OKOKOKOK")
        self.openLogWindow(item)

    def handle_stopall(self):
        data_row = self.model.getAllData()
        # if data_row[0] not in self.threads:
        count = 1
        for i in data_row[1:]:
            if i[0] in self.threads and self.threads[i[0]] is not None:
                self.threads[i[0]].pause()
                self.model.data_row_color(count)
                self.model.changeStatus(count, False)
                self.btn_start.setEnabled(False)
                print("Stop thread")
            count += 1
        pass


    def handle_stop(self):
        token = self.token.toPlainText()
        if len(token) == 0:
            print("missing token !!!")
            return
        if len(self.data) <= 1:
            return

        print("Hello")
        data_row = self.model.data_row(self.currentRow.row())

        if data_row[0] in self.threads and self.threads[data_row[0]] is not None:
            # self.threads[data_row[0]].join()
            # self.threads[data_row[0]]. file_score.close()
            self.threads[data_row[0]].pause()
            # self.threads[data_row[0]] = None
            # self.threads[data_row[0]].join()
            self.model.data_row_color(self.currentRow.row())
            self.model.changeStatus(self.currentRow.row(), False)
            self.btn_start.setEnabled(False)
            print("Stop thread")
            # d = DeviceBitable(data_row, self.token.toPlainText())
            # self.threads[data_row[0]] = threading.Thread(target=d.run, args=())

            # self.model.data_row_color(self.currentRow.row())
            # self.model.changeStatus(self.currentRow.row(), True)
        # pass

    # def run(self):

    def handle_start(self):
        token = self.token.toPlainText()
        if len(token) == 0:
            print("missing token !!!")
            return
        if len(self.data) <= 1:
            return

        data_row = self.model.data_row(self.currentRow.row())
        # if data_row[0] not in self.threads:

        if data_row[0] in self.threads and self.threads[data_row[0]] is None:
            # d = DeviceBitable(data_row, self.token.toPlainText())
            # self.threads[data_row[0]] = thread_with_trace(target=d.run, args=())
            # a = thread_with_trace(target=d.run, args=())

            # self.threads[data_row[0]].start()
            # t = threading.Thread(target=d.run, args=())

            self.threads[data_row[0]] = DeviceBitable(data_row, self.token.toPlainText())
            # a = thread_with_trace(target=d.run, args=())
            self.threads[data_row[0]].status = 1
            self.threads[data_row[0]].start()
            self.btn_start.setEnabled(False)
            self.btn_stop.setEnabled(True)
            self.model.data_row_color(self.currentRow.row())
            self.model.changeStatus(self.currentRow.row(), True)
        elif data_row[0] in self.threads and self.threads[data_row[0]] is not None:
            self.threads[data_row[0]].continues()
            self.btn_start.setEnabled(False)
            self.btn_stop.setEnabled(True)
            self.model.data_row_color(self.currentRow.row())
            self.model.changeStatus(self.currentRow.row(), True)

    def add_new(self):
        name_device = self.name.text()
        self.add_device_to_list(name_device)

    def func_test(self, item):

        # print(item.column(), item.row())

        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setPlaceholderText(_translate("MainWindow", "Tên thiết bị"))
        self.add_device.setText(_translate("MainWindow", "Add"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.btn_startall.setText(_translate("MainWindow", "Start ALL"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.btn_stopall.setText(_translate("MainWindow", "Stop All"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
