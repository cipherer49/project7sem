import socket
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QDialog, QApplication,QMessageBox,QTableWidgetItem
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PyQt5.uic import loadUi
import sys
sys.path.append('D:/panapticon/scanner/dns_conversion.py')
from scanner.dns_conversion import fetch_dns_data_from_database, dns_to_ip



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
        self.add_btn.clicked.connect(self.store_Dns_Data)# to call function to store dns to sql
        self.loadAndPopulateData()# to showing the sql stored data into pyqt table
        self.rem_btn.clicked.connect(self.deleteRowByID)
        self.dns_filter_apply_btn.clicked.connect(self.dns_apply_Message)
        self.dns_filter_rem_btn.clicked.connect(self.dns_remove_Message)
        self.dns_filter_rem_btn.clicked.connect(self.getRowCount)
        self.dns_filter_apply_btn.clicked.connect(self.getRowCount2)
        self.dns_filter_apply_btn.clicked.connect(self.dns_to_ip_show)# for fetching from dns and converting to ip then showing it




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
        dns = []
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

    def store_Dns_Data(self):
        # Connect to an SQLite database
        conn = sqlite3.connect('dns_database.db')
        cursor = conn.cursor()

        # Create a table (if it doesn't exist) to store the data
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ip_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                column1 INTEGER,
                column2 TEXT
            )
        ''')

        # Iterate through the table and insert data into the database
        for row_index in range(self.iptable.rowCount()):
            column1 = self.iptable.item(row_index, 0).text()
            column2 = self.iptable.item(row_index, 1).text()

            # Insert data into the database
            cursor.execute('INSERT INTO ip_data (column1, column2) VALUES (?, ?)', (column1, column2))

        # Commit the changes and close the connection
        conn.commit()
        # Fetch and print the inserted data
        cursor.execute('SELECT * FROM ip_data')
        inserted_data = cursor.fetchall()

        for row in inserted_data:
            print(f'ID: {row[0]}, Column1: {row[1]}, Column2: {row[2]}')

        # Close the connection
        conn.close()

        print('Data stored in SQL database.')

    def deleteRowByID(self):
        id_to_delete = self.rem_ip.text()

        if id_to_delete:
            # Connect to the SQLite database
            conn = sqlite3.connect('dns_database.db')
            cursor = conn.cursor()

            # Delete the row with the specified ID
            cursor.execute('DELETE FROM ip_data WHERE column1 = ?', (id_to_delete,))

            # Commit the changes
            conn.commit()
            conn.close()

            # Refresh the table to reflect the changes
            self.loadAndPopulateData()
            print(f'Removed rows with ID {id_to_delete} from SQL database.')

    def loadAndPopulateData(self):
        # Connect to the SQLite database
        conn = sqlite3.connect('dns_database.db')
        cursor = conn.cursor()

        # Execute a SELECT query to retrieve data from the database
        cursor.execute('SELECT * FROM ip_data')

        # Fetch all the rows from the query result
        rows = cursor.fetchall()

        # Populate the table with retrieved data
        self.iptable.setRowCount(len(rows))
        for row_index, row in enumerate(rows):
            id_item = QTableWidgetItem(str(row[1]))  # Assuming ID is in the second column
            ip_item = QTableWidgetItem(row[2])  # Assuming IP is in the third column

            self.iptable.setItem(row_index, 0, id_item)
            self.iptable.setItem(row_index, 1, ip_item)

        # Close the database connection
        conn.close()



    def getRowCount(self):
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('dns_database.db')
            cursor = conn.cursor()

            # Execute a SQL query to count the rows in the 'ip_data' table
            cursor.execute('SELECT COUNT(*) FROM ip_data')
            row_count = cursor.fetchone()[0]



            self.dns_remove_Message(row_count)


            #self.dns_display_label.setText(f'Total Rows: {row_count}')
            # Close the database connection
            conn.close()


        except Exception as e:
            print(f"Error: {str(e)}")

    def getRowCount2(self):
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('dns_database.db')
            cursor = conn.cursor()

            # Execute a SQL query to count the rows in the 'ip_data' table
            cursor.execute('SELECT COUNT(*) FROM ip_data')
            row_count = cursor.fetchone()[0]



            self.dns_apply_Message(row_count)


            #self.dns_display_label.setText(f'Total Rows: {row_count}')
            # Close the database connection
            conn.close()


        except Exception as e:
            print(f"Error: {str(e)}")

    def dns_apply_Message(self,row_count):#showing message of applied or not
        message_style = """
                            color: blue;
                        """
        self.dns_display_label.setStyleSheet(message_style)
        # Display a message in the QLabel
        self.dns_display_label.setText(f"Action applied for dns [{row_count}].\n This message remains visible.")

    def dns_remove_Message(self,row_count):
        message_style = """
                    color: red;
                """
        self.dns_display_label.setStyleSheet(message_style)
        self.dns_display_label.setText(f"Action Removed from dns [{row_count}]\nThis message remains visible")

    def dns_to_ip_show(self):
        dns_data = fetch_dns_data_from_database()  # Fetch DNS data from the database

        for dns_name_tuple in dns_data:
            column1, dns_name = dns_name_tuple  # Unpack the tuple into column1 and dns_name
            try:
                ip_address = socket.gethostbyname(dns_name)
                print(f"Id: {column1}, DNS Name: {dns_name}, IP Address: {ip_address}")
            except socket.gaierror as e:
                print(f"Id: {column1}, DNS Name: {dns_name}, Error: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Config_scr()
    window.show()
    sys.exit(app.exec_())




