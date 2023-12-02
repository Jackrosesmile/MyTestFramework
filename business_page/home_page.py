from ..common.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    HOME_LOGO = (By.XPATH, "//*[@id='header']//img[@src='/static/images/home/logo.png']")
    HOME = (By.XPATH, "//a[@href='/' and @style='color: orange;']")
    PRODUCTS = (By.XPATH, "//a[@href='/products']")
    CART = (By.XPATH, "//li/a[@href='/view_cart']")
    LOGIN = (By.XPATH, "//a[@href='/login']")
    LOGOUT = (By.XPATH, "//a[@href='/logout']")
    CONTACT = (By.XPATH, "//a[@href='/contact_us']")

    def get_home_logo(self, **kwargs):
        return self.element_is_existence(self.HOME_LOGO, **kwargs)

    def click_home(self, **kwargs):
        self.click(self.HOME, **kwargs)

    def click_products(self, **kwargs):
        self.click(self.PRODUCTS, **kwargs)

    def click_cart(self, **kwargs):
        self.click(self.CART, **kwargs)

    def click_contact(self, **kwargs):
        self.click(self.CONTACT, **kwargs)

    def click_login(self, **kwargs):
        self.click(self.LOGIN, **kwargs)

    def click_logout(self, **kwargs):
        self.click(self.LOGOUT, **kwargs)


