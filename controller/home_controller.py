import logging

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QBrush, QColor, QPalette, QPixmap, QRegExpValidator, QIntValidator
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QLineEdit, QAbstractItemView, QHeaderView, QTableWidget, \
    QTableWidgetItem, QMainWindow, QDesktopWidget, QAction
from cushy_storage import CushyDict

from pages.home import Ui_MainWindow


class HomeController(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_attr()
        self.init_slot()

        self.logger = logging.getLogger(__name__)

    def init_attr(self):
        self.setWindowTitle("Home Page")

    def init_slot(self):
        pass
