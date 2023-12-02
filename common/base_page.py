from loguru import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, ec=True, wait_time=20, poll_frequency=0.5, click=False):
        """
        :param locator: 传入的元素定位器及对应的值，如：By.ID, By.NAME, By.CLASS_NAME, By.TAG_NAME, By.XPATH
        :param ec: 设置是否使用显式等待，默认使用
        :param wait_time: 传入的等待时间，默认20
        :param poll_frequency: 设置多久轮训一次，默认0.5
        :param click: 设置是否等待元素可被点击，默认等待元素可见
        :return: 返回元素对象
        """
        element = None
        if ec:
            try:
                if click:
                    logger.info(f"等待元素可被点击：{locator}, 等待时间：{wait_time}秒。")
                    element = WebDriverWait(self.driver, timeout=wait_time, poll_frequency=poll_frequency).until(
                        EC.element_to_be_clickable(locator))
                else:
                    logger.info(f"等待元素可见：{locator}, 等待时间：{wait_time}秒。")
                    element = WebDriverWait(self.driver, timeout=wait_time, poll_frequency=poll_frequency).until(
                        EC.visibility_of_element_located(locator))
            except (NoSuchElementException, TimeoutException) as e:
                logger.error(f"定位元素失败或等待超时：{locator}, 错误信息：{str(e)}。")
                raise e
        else:
            try:
                logger.info(f"尝试定位元素：{locator}")
                element = self.driver.find_element(*locator)
            except Exception as e:
                logger.error(f"定位元素失败：{locator}, 错误信息：{str(e)}。")
                raise e
        return element

    def click(self, locator, **kwargs):
        """
        :param locator: 传入的元素定位器及对应的值，如：By.ID, By.NAME, By.CLASS_NAME
        :param kwargs: 传入的参数，如：ec=True, wait_time=20, poll_frequency=0.5, click=False
        ec: 设置是否使用显式等待，默认使用
        wait_time: 传入的等待时间，默认20
        poll_frequency: 设置多久轮训一次，默认0.5
        click: 设置是否等待元素可被点击，默认等待元素可被点击
        """
        if 'click' not in kwargs:
            kwargs['click'] = True
        element = self.find_element(locator, **kwargs)
        try:
            logger.info(f"点击元素：{locator}")
            element.click()
        except Exception as e:
            logger.error(f"点击元素{locator}时发生错误：{e}")

    def js_click(self, locator, **kwargs):
        if 'click' not in kwargs:
            kwargs['click'] = True
        element = self.find_element(locator, **kwargs)
        try:
            logger.info(f"使用js点击元素：{locator}")
            self.driver.execute_script('arguments[0].click()', element)
        except Exception as e:
            logger.error(f"使用js点击元素{locator}时发生错误：{e}")

    def input_text(self, locator, text, **kwargs):
        """
        :param text:
        :param locator: 传入的元素定位器及对应的值，如：By.ID, By.NAME, By.CLASS_NAME
        :param kwargs: 传入的参数，如：ec=True, wait_time=20, poll_frequency=0.5, click=False
        ec: 设置是否使用显式等待，默认使用
        wait_time: 传入的等待时间，默认20
        poll_frequency: 设置多久轮训一次，默认0.5
        click: 设置是否等待元素可被点击，默认等待元素可见
        """
        element = self.find_element(locator, **kwargs)
        element.clear()
        try:
            logger.info(f"在元素：{locator} 中输入文本{text}。")
            element.send_keys(text)
        except Exception as e:
            logger.error(f"在输入文本{text}时发生错误：{e}")

    # 获取元素的文本二次封装
    def get_text(self, locator, **kwargs):
        logger.info(f'获取元素的文本:{locator}')
        return self.find_element(locator, **kwargs).text

    # 判断元素是否存在
    def element_is_existence(self, locator, **kwargs):
        logger.info(f'判断元素是否存在:{locator}')
        element = self.find_element(locator, **kwargs)
        return element

    # input标签的文件上传
    def input_upload(self, locator, filepath, **kwargs):
        if 'click' not in kwargs:
            kwargs['click'] = True
        self.find_element(locator, **kwargs).send_keys(filepath)
