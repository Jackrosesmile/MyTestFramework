from ..action_layer.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    LOGIN = (By.CSS_SELECTOR, 'a i.fa.fa-lock')
    USERNAME_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-qa="login-button"]')

    def click_login(self, wait_flag=False, timeout=10):
        self.click(self.LOGIN, wait_flag, timeout)

    def input_username(self, username, wait_flag=False, timeout=10):
        self.input_text(self.USERNAME_INPUT, username, wait_flag, timeout)

    def input_password(self, password, wait_flag=False, timeout=10):
        self.input_text(self.PASSWORD_INPUT, password, wait_flag, timeout)

    def click_login_button(self, wait_flag=False, timeout=10):
        self.click(self.LOGIN_BUTTON, wait_flag, timeout)
