import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        try:
            logging.info(f"尝试定位元素：{locator}")
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            logging.error(f"元素定位失败：{locator}。请确认元素定位方式是否正确，或考虑使用等待机制。")
            raise Exception(f"元素定位失败：{locator}。请确认元素选择器是否正确，或尝试使用等待方法。")

    def wait_for_element(self, locator, timeout=10):
        try:
            logging.info(f"等待元素可见：{locator}, 超时时间：{timeout}秒。")
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            logging.error(f"元素未在指定时间{timeout}秒内出现：{locator}。请检查元素是否正确，或尝试增加等待时间。")
            raise Exception(f"等待元素超时：{locator}。请确认元素选择器是否正确，或考虑增加等待时间超过 {timeout} 秒。")

    def click(self, locator, wait_flag=False, timeout=10):
        try:
            if wait_flag:
                element = self.wait_for_element(locator, timeout)
            else:
                element = self.find_element(locator)
            logging.info(f"点击元素：{locator}")
            element.click()
        except Exception as e:
            logging.error(f"点击元素{locator}时发生错误：{e}")
            raise

    def input_text(self, locator, text, wait_flag=False, timeout=10):
        try:
            if wait_flag:
                element = self.wait_for_element(locator, timeout)
            else:
                element = self.find_element(locator)
            logging.info(f"在元素：{locator} 中输入文本{text}。")
            element.send_keys(text)
        except Exception as e:
            logging.error(f"在输入文本{text}时发生错误：{e}")
            raise
