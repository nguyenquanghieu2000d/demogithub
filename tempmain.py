# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
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
        self.start_test = QtWidgets.QPushButton(self.centralwidget)
        self.start_test.setGeometry(QtCore.QRect(280, 510, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.start_test.setFont(font)
        self.start_test.setObjectName("start_test")
        self.list_device = QtWidgets.QTableView(self.centralwidget)
        self.list_device.setGeometry(QtCore.QRect(20, 150, 1131, 351))
        self.list_device.setObjectName("list_device")
        self.token = QtWidgets.QTextEdit(self.centralwidget)
        self.token.setGeometry(QtCore.QRect(20, 80, 1131, 61))
        self.token.setObjectName("token")
        self.start_test_2 = QtWidgets.QPushButton(self.centralwidget)
        self.start_test_2.setGeometry(QtCore.QRect(20, 510, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.start_test_2.setFont(font)
        self.start_test_2.setObjectName("start_test_2")
        self.start_test_3 = QtWidgets.QPushButton(self.centralwidget)
        self.start_test_3.setGeometry(QtCore.QRect(550, 510, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.start_test_3.setFont(font)
        self.start_test_3.setObjectName("start_test_3")
        self.start_test_4 = QtWidgets.QPushButton(self.centralwidget)
        self.start_test_4.setGeometry(QtCore.QRect(850, 510, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.start_test_4.setFont(font)
        self.start_test_4.setObjectName("start_test_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setPlaceholderText(_translate("MainWindow", "Tên thiết bị"))
        self.add_device.setText(_translate("MainWindow", "Add"))
        self.start_test.setText(_translate("MainWindow", "Start"))
        self.start_test_2.setText(_translate("MainWindow", "Start ALL"))
        self.start_test_3.setText(_translate("MainWindow", "Stop"))
        self.start_test_4.setText(_translate("MainWindow", "Stop All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())