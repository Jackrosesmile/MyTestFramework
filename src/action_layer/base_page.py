from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # def get_element(self, locator_type):
    #     by_type = getattr(By, locator_type.upper(), None)
    #     if by_type is None:
    #         raise ValueError(f"Locator type {locator_type} not found in By class")
    #     return by_type

    # def find_element(self, locator_type, locator_value):
    #     # by_type = self.get_element(locator_type)
    #     # return self.driver.find_element(by_type,locator_value)

    def click(self, locator_type, locator_value):
        self.driver.find_element(locator_type, locator_value).click()

    def input_text(self, locator_type, locator_value, text):
        self.driver.find_element(locator_type, locator_value).send_keys(text)

    # 等待元素的方法现在接受一个超时时间参数
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
