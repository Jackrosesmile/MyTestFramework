from ..common.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-qa="login-button"]')
    LOGIN_CORRECT = (By.XPATH, "//*[contains(text(),'Logged in as')]")
    LOGIN_INCORRECT = (By.XPATH, "//p[text()='Your email or password is incorrect!']")

    def input_username(self, username, **kwargs):
        self.input_text(self.USERNAME_INPUT, username, **kwargs)

    def input_password(self, password, **kwargs):
        self.input_text(self.PASSWORD_INPUT, password, **kwargs)

    def click_login_button(self, **kwargs):
        self.click(self.LOGIN_BUTTON, **kwargs)

    def get_login_correct(self, **kwargs):
        return self.get_text(self.LOGIN_CORRECT, **kwargs)

    def get_login_incorrect(self, **kwargs):
        return self.get_text(self.LOGIN_INCORRECT, **kwargs)

