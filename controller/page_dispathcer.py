import logging

from controller.register_controller import RegisterController
from controller.login_controller import LoginController
from controller.home_controller import HomeController


class PageDispatcher:
    """
    application page dispatcher,用作页面调度,控制不同的页面,负责处理不同页面跳转的逻辑
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug('page dispatcher startup')

    def show_page_login(self):
        self.page_login = LoginController()
        self.page_login.show()
        self.page_login.to_register_page_signal.connect(self.show_page_register)
        self.page_login.to_home_page_signal.connect(self.show_page_home)

    def show_page_register(self):
        self.page_register = RegisterController()
        self.page_register.show()

    def show_page_home(self):
        self.page_home = HomeController()
        self.page_home.show()
