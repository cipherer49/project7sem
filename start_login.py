# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from tkinter import messagebox
from start_screen import Start_scr
from PyQt5.uic import loadUi

class Ui_start_login_window(object):

    # for start_login_btn
    def start_log_btn(self):
        print("start login button clicked")
        sh_input = self.shared_pwd_input.text()
        con = sqlite3.connect(database=r'login.db')
        cursor = con.cursor()
        query = "SELECT * FROM start_login_table WHERE sh_pwd =?"
        cursor.execute(query, (sh_input,))
        result = cursor.fetchone()
        if result:
            print("Login is successful!")
            # Perform actions for successful login here, e.g., show the main application window.
            messagebox.showinfo("showinfo", "Login Successful")
            from start_screen import Start_scr
            self.show_start_window()


        else:
            print("Login failed. Invalid username or password.")
            # Show an error message to the user indicating invalid login credentials.
            messagebox.askretrycancel("askretrycancel", "Incorrect username or password Try again")
        con.close()
        pass
    def show_start_window(self):

        self.start_window = Start_scr()
        
        self.start_window.show()
    def setupUi(self, start_login_window):
        start_login_window.setObjectName("start_login_window")
        start_login_window.setWindowModality(QtCore.Qt.NonModal)
        start_login_window.setEnabled(True)
        start_login_window.resize(600, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(98)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(start_login_window.sizePolicy().hasHeightForWidth())
        start_login_window.setSizePolicy(sizePolicy)
        start_login_window.setMinimumSize(QtCore.QSize(600, 800))
        start_login_window.setAutoFillBackground(False)
        start_login_window.setStyleSheet("background-color:#003366;")
        self.centralwidget = QtWidgets.QWidget(start_login_window)
        self.centralwidget.setObjectName("centralwidget")
        self.pwd_label = QtWidgets.QLabel(self.centralwidget)
        self.pwd_label.setGeometry(QtCore.QRect(180, 390, 121, 51))
        self.pwd_label.setObjectName("pwd_label")
        self.lstart_login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.lstart_login_btn.setGeometry(QtCore.QRect(370, 510, 81, 41))
        self.lstart_login_btn.setStyleSheet("background-color:white;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lstart_login_btn.setIcon(icon)
        self.lstart_login_btn.setObjectName("lstart_login_btn")
        #it is called here start_login_btn
        self.lstart_login_btn.clicked.connect(self.start_log_btn)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 230, 291, 61))
        self.label_4.setObjectName("label_4")
        self.start_back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_back_btn.setGeometry(QtCore.QRect(220, 510, 91, 41))
        self.start_back_btn.setStyleSheet("background-color:white;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("back-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_back_btn.setIcon(icon1)
        self.start_back_btn.setObjectName("start_back_btn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 120, 91, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("shared-vision.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 230, 61, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("login.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.shared_pwd_input = QtWidgets.QLineEdit(self.centralwidget)
        self.shared_pwd_input.setGeometry(QtCore.QRect(310, 410, 161, 31))
        self.shared_pwd_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.shared_pwd_input.setStyleSheet("font-size:12pt;color: rgb(0, 0, 0);background-color:\"white\";")
        self.shared_pwd_input.setObjectName("shared_pwd_input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 310, 291, 31))
        self.label.setObjectName("label")
        start_login_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(start_login_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        start_login_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(start_login_window)
        self.statusbar.setObjectName("statusbar")
        start_login_window.setStatusBar(self.statusbar)

        self.retranslateUi(start_login_window)
        QtCore.QMetaObject.connectSlotsByName(start_login_window)

    def retranslateUi(self, start_login_window):
        _translate = QtCore.QCoreApplication.translate
        start_login_window.setWindowTitle(_translate("start_login_window", "MainWindow"))
        self.pwd_label.setText(_translate("start_login_window", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Password:</span></p></body></html>"))
        self.lstart_login_btn.setText(_translate("start_login_window", "LOGIN"))
        self.label_4.setText(_translate("start_login_window", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#ff0000;\">LOGIN</span></p></body></html>"))
        self.start_back_btn.setText(_translate("start_login_window", "BACK"))
        self.label.setText(_translate("start_login_window", "<html><head/><body style =\"color:yellow\"><p align=\"center\">ENTER THE SHARED PASSWORD</p></body></html>"))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    start_login_window = QtWidgets.QMainWindow()
    ui = Ui_start_login_window()
    ui.setupUi(start_login_window)
    start_login_window.show()
    sys.exit(app.exec_())
