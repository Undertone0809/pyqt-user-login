import logging
import hashlib

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp, pyqtSlot
from PyQt5.QtGui import QBrush, QColor, QPalette, QPixmap, QRegExpValidator, QIntValidator
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QLineEdit, QAbstractItemView, QHeaderView, QTableWidget, \
    QTableWidgetItem, QMainWindow, QDesktopWidget, QAction
from cushy_storage import CushyDict

from pages.register import Ui_MainWindow


class RegisterController(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_attr()
        self.init_slot()

        self.cache = CushyDict('./cache')
        self.logger = logging.getLogger(__name__)

    def init_attr(self):
        self.setWindowTitle("Register Page")

    def init_slot(self):
        self.btn_register.clicked.connect(self.register)

    def register(self):
        account = self.lineEdit_account.text()
        password = self.lineEdit_password.text()
        self.logger.debug(f"[user] account: {account} password: {password}")

        # 创建md5对象
        m = hashlib.md5()
        # 更新md5加密内容
        m.update(password.encode('utf-8'))
        # 获取加密后的字符串，以16进制输出
        result = m.hexdigest()

        self.logger.debug(result)
        self.cache[account] = result
        QMessageBox.about(self, "提示", "注册成功")
        self.close()
