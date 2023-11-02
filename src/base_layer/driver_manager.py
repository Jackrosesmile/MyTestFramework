from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class DriverManager:
    def __init__(self, config):
        self.driver = None
        browser_type = config['browse']['type']
        driver_path = config['browse']['path']

        if browser_type.lower() == "chrome":
            chrome_options = Options()
            chrome_options.binary_location = ("/Applications/Google Chrome for Testing.app/Contents/MacOS/Google "
                                              "Chrome for Testing")
            service = Service(executable_path=driver_path)
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
        elif browser_type.lower() == "firefox":
            self.driver = webdriver.Firefox(executable_path=driver_path)
        elif browser_type.lower() == "safari":
            self.driver = webdriver.Safari(executable_path=driver_path)
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")

    def get_driver(self):
        return self.driver
