from ..common.base_page import BasePage
from selenium.webdriver.common.by import By


class ContactUsPage(BasePage):
    NAME = (By.XPATH, '//form[@id="contact-us-form"]//input[@type="text" and @name="name"]')
    EMAIL = (By.XPATH, '//form[@id="contact-us-form"]//input[@type="email" and @name="email"]')
    SUBJECT = (By.XPATH, '//form[@id="contact-us-form"]//input[@type="text" and @name="subject"]')
    MESSAGE = (By.ID, 'message')
    CHOOSE_FILE = (By.XPATH, '//form[@id="contact-us-form"]//input[@type="file" and @name="upload_file"]')
    SUBMIT = (By.XPATH, '//form[@id="contact-us-form"]//input[@type="submit" and @name="submit"]')
    SUCCESS_MESSAGE = (By.XPATH, '//h2[@class="title text-center"]/following-sibling::div[text()="Success! Your '
                                 'details have been submitted successfully."]')

    def input_name(self, name, **kwargs):
        self.input_text(self.NAME, name, **kwargs)

    def input_email(self, email, **kwargs):
        self.input_text(self.EMAIL, email, **kwargs)

    def input_subject(self, subject, **kwargs):
        self.input_text(self.SUBJECT, subject, **kwargs)

    def input_message(self, message, **kwargs):
        self.input_text(self.MESSAGE, message, **kwargs)

    def choose_file(self, file_path, **kwargs):
        self.input_upload(self.CHOOSE_FILE, file_path, **kwargs)

    def click_submit(self, **kwargs):
        self.click(self.SUBMIT, **kwargs)

    def is_success(self, **kwargs):
        return self.element_is_existence(self.SUCCESS_MESSAGE, **kwargs)



