from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QDialog, QApplication,QMessageBox
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PyQt5.uic import loadUi
import sys

#for implementing new screen from config_login button we create a class
class Start_scr(QtWidgets.QMainWindow):
    def __init__(self,):
        super(Start_scr,self).__init__()
        loadUi("start_page.ui",self)

