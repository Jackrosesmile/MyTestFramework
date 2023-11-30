from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class DriverManager:
    def __init__(self, config):
        self.driver = None
        browser_type = config['browse']['type']
        driver_path = config['browse']['path']
        binary_path = config['browse']['binary_path']
        if browser_type.lower() == "chrome":
            if binary_path == '' or driver_path == '' or binary_path is None or driver_path is None:
                self.driver = webdriver.Chrome()
            else:
                # options指定浏览器的路径二进制文件
                chrome_options = webdriver.ChromeOptions()
                chrome_options.binary_location = binary_path
                # service指定webdriver路径
                service = webdriver.ChromeService(executable_path=driver_path)
                self.driver = webdriver.Chrome(service=service, options=chrome_options)
        elif browser_type.lower() == "edge":
            if binary_path == '' or driver_path == '' or binary_path is None or driver_path is None:
                self.driver = webdriver.Edge()
            else:
                edge_options = webdriver.EdgeOptions()
                edge_options.binary_location = binary_path
                service = webdriver.EdgeService(executable_path=driver_path)
                self.driver = webdriver.Edge(service=service, options=edge_options)
        elif browser_type.lower() == "firefox":
            if binary_path == '' or driver_path == '' or binary_path is None or driver_path is None:
                self.driver = webdriver.Firefox()
            else:
                firefox_options = webdriver.FirefoxOptions()
                firefox_options.binary_location = binary_path
                service = webdriver.FirefoxService(executable_path=driver_path)
                self.driver = webdriver.Firefox(service=service, options=firefox_options)
        elif browser_type.lower() == "safari":
            self.driver = webdriver.Safari()
        else:
            raise ValueError(f"不支持的浏览器: {browser_type}，请使用以下浏览器运行【chrome】，【edge】，【firefox】，【safari】")

    def get_driver(self):
        return self.driver
