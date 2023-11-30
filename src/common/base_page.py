from loguru import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, wait_time=None):
        element = None
        try:
            if wait_time:
                logger.info(f"等待元素可见：{locator}, 等待时间：{wait_time}秒。")
                element = WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(locator))
            else:
                logger.info(f"尝试定位元素：{locator}")
                element = self.driver.find_element(*locator)
        except (NoSuchElementException, TimeoutException) as e:
            logger.error(f"定位元素失败或等待超时：{locator}, 错误信息：{str(e)}。")
            raise e
        return element

    def click(self, locator, wait_time=None):
        element = self.find_element(locator, wait_time)
        try:
            logger.info(f"点击元素：{locator}")
            element.click()
        except Exception as e:
            logger.error(f"点击元素{locator}时发生错误：{e}")
            # raise

    def input_text(self, locator, text, wait_time=None):
        element = self.find_element(locator, wait_time)
        try:
            logger.info(f"在元素：{locator} 中输入文本{text}。")
            element.send_keys(text)
        except Exception as e:
            logger.error(f"在输入文本{text}时发生错误：{e}")
            # raise
