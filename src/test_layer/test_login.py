import pytest
from ..business_layer.login_page import LoginPage
from ..utils_layer.file_handler import read_yaml
from ..base_layer.driver_manager import DriverManager


class TestLogin:
    #@pytest.mark.parametrize("username, password", read_yaml("login_credentials.yaml"))
    @pytest.mark.parametrize("test_input", read_yaml('src/test_layer/test_data.yaml')['test_login'])
    def test_user_login(self, driver_manager, test_input):
        username = test_input['username']
        password = test_input['password']
        login_page = LoginPage(driver_manager)
        login_page.click_login()
        login_page.input_username(username)
        login_page.input_password(password)
        login_page.click_login_button()
