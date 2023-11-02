from ..action_layer.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    LOGIN = (By.CSS_SELECTOR, 'a i.fa.fa-lock')
    USERNAME_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-qa="login-button"]')

    def click_login(self):
        self.click(*self.LOGIN)

    def input_username(self, username):
        self.input_text(*self.USERNAME_INPUT, username)

    def input_password(self, password):
        self.input_text(*self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(*self.LOGIN_BUTTON)
