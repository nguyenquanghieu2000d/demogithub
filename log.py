# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtCore import Qt, QTime, QDateTime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush
import json
from datetime import datetime


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        if role == Qt.BackgroundRole:
            if self._data[index.row()][3] == "type_mess":
                pass
            elif self._data[index.row()][3] == "1":
                return QBrush(Qt.green)
            else:
                return QBrush(Qt.red)

    # def _data(self):

    def data_col_row(self, row_index, col_index, role):
        if role == Qt.DisplayRole:
            return self._data[row_index][col_index]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class Ui_Form(object):
    def setupUi(self, Form, Name):
        Form.setObjectName("Form")
        Form.resize(906, 671)
        self.listlog = QtWidgets.QTableView(Form)
        self.listlog.setGeometry(QtCore.QRect(30, 190, 851, 451))
        self.listlog.setObjectName("listlog")
        self.listlog.horizontalHeader().setMinimumSectionSize(100)
        self.message = QtWidgets.QLabel(Form)
        self.message.setGeometry(QtCore.QRect(96, 543, 401, 21))
        self.message.setText("")
        self.message.setObjectName("message")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lbName = QtWidgets.QLabel(Form)
        self.lbName.setGeometry(QtCore.QRect(110, 30, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbName.setFont(font)
        self.lbName.setObjectName("lbName")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(340, 40, 151, 31))
        self.comboBox.setObjectName("comboBox")
        self.start_time = QtWidgets.QDateTimeEdit(Form)
        self.start_time.setGeometry(QtCore.QRect(650, 10, 194, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start_time.setFont(font)
        self.start_time.setObjectName("start_time")
        self.end_time = QtWidgets.QDateTimeEdit(Form)
        self.end_time.setGeometry(QtCore.QRect(650, 50, 194, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.end_time.setFont(font)
        self.end_time.setObjectName("end_time")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(540, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(540, 60, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(260, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnTimKiem = QtWidgets.QPushButton(Form)
        self.btnTimKiem.setGeometry(QtCore.QRect(280, 110, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnTimKiem.setFont(font)
        self.btnTimKiem.setObjectName("btnTimKiem")
        # self.listlog.horizontalHeader().hori
        # self.listlog.setColumnWidth(500)
        self.setupDefaultTime()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.currentComboBoxSelectedIndex = 0
        self.comboBox_data = ["Tất cả", "Wifi", "LAN", "bluetooth"]
        self.comboBox.clear()
        self.comboBox.addItems(self.comboBox_data)
        self.Name = Name
        self.listlog.setColumnWidth(0, 400)
        self.data = [
            ["time", "type", "mess", "type_mess"]
        ]
        self.log_path = "logs/" + Name + ".log"
        self.loadData(type="All",
                      date_start=self.start_time.dateTime().toPyDateTime(),
                      date_end=self.end_time.dateTime().toPyDateTime())
        # print(self.log_path)
        self.message = QtWidgets.QLabel(Form)
        self.message.setGeometry(QtCore.QRect(96, 543, 401, 21))
        self.message.setText("")
        self.message.setObjectName("message")
        self.listlog.setColumnWidth(0, 250)
        self.listlog.setColumnWidth(1, 100)
        self.listlog.setColumnWidth(2, 400)
        self.listlog.setColumnWidth(3, 0)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.event()

    def setupDefaultTime(self):

        datetime_object = QDateTime(2000, 1, 1, 0, 0, 0, 0, 0)
        self.start_time.setDateTime(datetime_object)

        datetime_object = QDateTime(2030, 1, 1, 0, 0, 0, 0, 0)
        self.end_time.setDateTime(datetime_object)

    def event(self):
        self.comboBox.activated.connect(self.setVal)
        self.btnTimKiem.clicked.connect(self.timKiem)

    def setVal(self, val):
        self.currentComboBoxSelectedIndex = val

    def timKiem(self):
        # print("OKOKOKOK")
        date_start = self.start_time.dateTime().toPyDateTime()
        # date_start = Time.strftime("%m/%d/%Y, %H:%M:%S")

        date_end = self.end_time.dateTime().toPyDateTime()
        # date_end = Time.strftime("%m/%d/%Y, %H:%M:%S")

        # print(date_time)
        if self.currentComboBoxSelectedIndex == 0:
            self.loadData("All", date_start=date_start, date_end=date_end)
        elif self.currentComboBoxSelectedIndex == 1:
            self.loadData("Wifi", date_start=date_start, date_end=date_end)
        elif self.currentComboBoxSelectedIndex == 2:
            self.loadData("LAN", date_start=date_start, date_end=date_end)
        elif self.currentComboBoxSelectedIndex == 3:
            self.loadData("bluetooth", date_start=date_start, date_end=date_end)
        # print("Hello")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(self.Name)
        self.label.setText(_translate("Form", "Tên thiết bị: "))
        self.lbName.setText(_translate("Form", self.Name))
        self.label_2.setText(_translate("Form", "Ngày bắt đầu:"))
        self.label_3.setText(_translate("Form", "Ngày kết thúc:"))
        self.label_4.setText(_translate("Form", "Thông tin:"))
        self.btnTimKiem.setText(_translate("Form", "TÌM KIẾM"))

    def loadData(self, type, date_start, date_end):
        # try:
        try:
            File = open(self.log_path, "r")
        except:
            File = open(self.log_path, "x")
        try:
            g = File.read().split("\n")
            g.reverse()
            self.data.clear()

            if type == "All":
                for i in g:
                    item = i.split("\t")
                    if len(item) > 1:
                        # print(item[0])
                        # print(str(date_end))
                        datetime_object = datetime.strptime(item[0], '%H:%M:%S %d-%m-%Y')
                        if date_start < datetime_object < date_end:
                            self.data.append([item[0], item[1], item[2], item[3]])

            else:
                for i in g:
                    item = i.split("\t")
                    if len(item) > 1:
                        datetime_object = datetime.strptime(item[0], '%H:%M:%S %d-%m-%Y')
                        if item[1] == type and date_start < datetime_object < date_end:
                            self.data.append([item[0], item[1], item[2], item[3]])
            print("------------------------------")
            print(len(self.data))
            if len(self.data) == 0:
                self.data = [
                    ["time", "type", "mess", "type_mess"]
                ]
            self.model = TableModel(self.data)
            self.listlog.setModel(self.model)
        except:
            pass
        # except Exception as e:
        #     print(e)
        #     print("File don't exists")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

from datetime import datetime


def write_log_file(device, type, mess, type_mess):
    file_score = open("./logs/Score.json", "r")
    a = file_score.read()
    file_score.close()
    file_score = open("./logs/Score.json", "w")

    # file_score_ = open("./logs/Score.json", "r")
    a_json = json.loads(a)

    try:
        k = a_json[device]
    except:
        a_json[device] = {
            "Wifi": [0, 0, 0],
            "LAN": [0, 0, 0],
            "bluetooth": [0, 0, 0]
        }
        k = a_json[device]
    # print("--------------------------")
    # print(json.dumps(k))
    # print( k[type][0])
    # print(k["LAN"][0])
    # print(k["Wifi"][0])
    if type_mess == 1:

        k[type][0] = k[type][0] + 1
        # k[1] = k[1] + 1
        k[type][2] = k[type][0] + k[type][1]
    else:
        k[type][1] = k[type][1] + 1
        k[type][2] = k[type][0] + k[type][1]
    a_json[device] = k
    a_text = json.dumps(a_json)
    file_score.write(a_text)
    file_score.close()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %d-%m-%Y")
    file_log = open("logs/{}.log".format(device), "a+")
    line = "{0}\t{1}\t{2}\t{3}\n".format(current_time, type, mess, type_mess)
    file_log.write(line)
    file_log.close()


def read_log_file(device):
    file_log = open("logs/{}.log".format(device), "r")
