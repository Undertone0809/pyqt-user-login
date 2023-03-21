import logging
import hashlib

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QBrush, QColor, QPalette, QPixmap, QRegExpValidator, QIntValidator
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QLineEdit, QAbstractItemView, QHeaderView, QTableWidget, \
    QTableWidgetItem, QMainWindow, QDesktopWidget, QAction
from cushy_storage import CushyDict

from pages.login import Ui_MainWindow


class LoginController(QtWidgets.QMainWindow, Ui_MainWindow):
    to_register_page_signal = QtCore.pyqtSignal()
    to_home_page_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_attr()
        self.init_slot()

        self.cache = CushyDict("./cache")
        self.logger = logging.getLogger(__name__)

    def init_attr(self):
        self.setWindowTitle("Login Page")
        self.lineEdit_account.setPlaceholderText("请输入帐号")
        self.lineEdit_password.setPlaceholderText("请输入密码")

    def init_slot(self):
        self.btn_login.clicked.connect(self.login)
        self.btn_register.clicked.connect(self.to_register_page)

    def login(self):
        account = self.lineEdit_account.text()
        password = self.lineEdit_password.text()
        self.logger.debug(f"[user] account: {account} password: {password}")
        self._validate_user(account, password)

    def _validate_user(self, account: str, password: str):
        if account in self.cache:
            m = hashlib.md5()
            m.update(password.encode('utf-8'))
            enc_pwd = m.hexdigest()

            if self.cache[account] == enc_pwd:
                self.logger.debug(enc_pwd)
                QMessageBox.about(self, "提示", "登陆成功")
                self.to_home_page_signal.emit()
            else:
                QMessageBox.about(self, "提示", "密码错误")
        else:
            QMessageBox.about(self, "提示", "帐号不存在，请注册")

    def to_register_page(self):
        self.to_register_page_signal.emit()
