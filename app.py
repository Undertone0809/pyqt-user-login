import sys
import logging
from PyQt5 import QtWidgets

from controller.login_controller import LoginController
from controller.register_controller import RegisterController
from controller.page_dispathcer import PageDispatcher


def enable_log():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# main Application
if __name__ == "__main__":
    enable_log()
    app = QtWidgets.QApplication(sys.argv)
    page_dispatcher = PageDispatcher()
    page_dispatcher.show_page_login()
    # page_dispatcher.show_page_register()
    sys.exit(app.exec_())
