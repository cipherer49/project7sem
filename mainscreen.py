# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from login_page import Ui_Login_window1
from start_login import Ui_start_login_window
from PyQt5.uic import loadUi

class Ui_MainWindow(object):
    # calling login page with login button
    def call_login(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Login_window1()
        self.ui.setupUi(self.window)
        MainWindow.hide()

        self.window.show()

    # for start_login function
    def start_btn(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_start_login_window()
        self.ui.setupUi(self.window2)
        MainWindow.hide()
        self.window2.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 608)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setStyleSheet("background-color:#003366")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setBaseSize(QtCore.QSize(0, 10))
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 70, 301, 61))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.start_button1 = QtWidgets.QPushButton(self.centralwidget)
        self.start_button1.setGeometry(QtCore.QRect(130, 390, 131, 41))
        self.start_button1.setAutoFillBackground(False)
        self.start_button1.setStyleSheet("background-color:\"white\";\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font-color:\"white\";\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("shuttle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_button1.setIcon(icon)
        self.start_button1.setObjectName("start_button1")
        #accessing start button
        self.start_button1.clicked.connect(self.start_btn)
        self.config_button1 = QtWidgets.QPushButton(self.centralwidget)
        self.config_button1.setGeometry(QtCore.QRect(300, 390, 141, 41))
        #accesing config button
        self.config_button1.clicked.connect(self.call_login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.config_button1.sizePolicy().hasHeightForWidth())
        self.config_button1.setSizePolicy(sizePolicy)
        self.config_button1.setStyleSheet("background-color:\"white\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("gear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.config_button1.setIcon(icon1)
        self.config_button1.setObjectName("config_button1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 370, 201))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 80, 61, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("shared-vision.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ff0000;\">Panopticon</span></p></body></html>"))
        self.start_button1.setText(_translate("MainWindow", "START"))
        self.config_button1.setText(_translate("MainWindow", "CONFIGURE"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body style=\"color:white\"><p align=\"center\">This NIDS is made for just Demonstration Purposes</p><p align=\"center\">Made By</p><p align=\"center\">Aryan(20IT1005)</p><p align=\"center\">Arsalaan(20IT1007)</p><p align=\"center\">Asif(20IT1004)</p><p align=\"center\">Kaif(20IT1019)</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.config_button1.clicked.connect(ui.call_login)

    # Store reference to MainWindow instance in Ui_MainWindow
    ui.main_window = MainWindow

    MainWindow.show()


    # Function to close the second window before application quits
    def close_second_window():
        if hasattr(ui, 'ui'):  # Check if the Ui_Login_window1 instance exists
            ui.ui.window.close()


    app.aboutToQuit.connect(close_second_window)  # Connect aboutToQuit signal
    sys.exit(app.exec_())
