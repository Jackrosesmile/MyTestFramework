import pytest
from ..business_page.login_page import LoginPage
from common.file_handler import read_yaml
from common.path import get_project_root

file_path = get_project_root('TestCase', 'test_data.yaml')


class TestLogin:
    @pytest.mark.parametrize("test_input", read_yaml(file_path)['test_login'])
    def test_user_login(self, driver_manager, config, test_input):
        username = test_input['username']
        password = test_input['password']
        driver_manager.get(config['env'])
        login_page = LoginPage(driver_manager)
        login_page.click_login()
        login_page.input_username(username, 3)
        login_page.input_password(password)
        login_page.click_login_button()
