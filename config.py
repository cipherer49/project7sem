from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QDialog, QApplication,QMessageBox,QTableWidgetItem
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PyQt5.uic import loadUi
import sys

#for implementing new screen from config_login button we create a class
class Config_scr(QtWidgets.QMainWindow):
    def __init__(self,):
        super(Config_scr,self).__init__()
        loadUi("config_page.ui",self)

        # Connect buttons to the slot function
        self.t_analysis_btn.clicked.connect(self.showPage1)
        self.extra_btn_1.clicked.connect(self.showPage2)
        self.extra_btn_2.clicked.connect(self.showPage3)
        self.loadIP()
        self.add_btn.clicked.connect(self.add_ip)
        self.rem_btn.clicked.connect(self.remove_ip)

    def add_ip(self):
        ID = self.id_input.text()
        IP = self.ip_input.text()
        if ID and IP is not None:
            rowCount = self.iptable.rowCount()
            self.iptable.insertRow(rowCount)
            self.iptable.setItem(rowCount,0,QTableWidgetItem(ID))
            self.iptable.setItem(rowCount, 1, QTableWidgetItem(IP))
    def remove_ip(self):
        ip_to_remove = self.rem_ip.text()

        # Find rows with a matching value in the 'Name' field and remove them
        for row in range(self.iptable.rowCount()):
            item = self.iptable.item(row, 1)  # Assuming 'IP' is in the second column (column 1)
            if item is not None and item.text() == ip_to_remove:
                self.iptable.removeRow(row)

    def showPage1(self):
        # Show page1 in the QStackedWidget
        self.pages.setCurrentWidget(self.page1)
        self.statuspages.setCurrentWidget(self.page01)

    def showPage2(self):
        # Show page2 in the QStackedWidget
        self.pages.setCurrentWidget(self.page2)
        self.statuspages.setCurrentWidget(self.page02)
    def showPage3(self):
        # Show page3 in the QStackedWidget
        self.pages.setCurrentWidget(self.page3)
        self.statuspages.setCurrentWidget(self.page03)

    def loadIP(self):
        # creating list variable for easy insertion
        dns = [

        ]
        self.iptable.setRowCount(len(dns))
        self.iptable.setColumnCount(2)
        self.iptable.setHorizontalHeaderLabels(('ID','DNS'))
        self.iptable.setColumnWidth(0,10)
        self.iptable.setColumnWidth(1,258)

        #LOOP TO PASS DATA IN THE table
        row_index = 0
        for ip in dns:

            self.iptable.setItem(row_index,0,QTableWidgetItem(str(ip['ID'])))
            self.iptable.setItem(row_index,1,QTableWidgetItem(str(ip['IP'])))
            row_index +=1

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Config_scr()
    window.show()
    sys.exit(app.exec_())



