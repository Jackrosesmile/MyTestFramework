import pytest

from ..business_page.home_page import HomePage
from ..business_page.login_page import LoginPage
from common.file_handler import read_yaml
from common.path import get_project_root

data_path = get_project_root('TestCase', 'test_login_data.yaml')


class TestLogin:
    @pytest.mark.parametrize("test_input", read_yaml(data_path)['login_account'])
    def test_user_login(self, driver_manager, config, test_input):
        username = test_input['username']
        password = test_input['password']
        assertname = test_input['assertname']
        driver_manager.get(config['url'])
        login_page = LoginPage(driver_manager)
        home_page = HomePage(driver_manager)
        assert home_page.get_home_logo()
        home_page.click_login(wait_time=3, poll_frequency=0.5)
        login_page.input_username(username, ec=False)
        login_page.input_password(password)
        login_page.click_login_button()
        if assertname == '登陆成功':
            assert 'Logged in as' in login_page.get_login_correct()
            home_page.click_logout()
            login_page_url = 'https://automationexercise.com/login'
            assert driver_manager.current_url == login_page_url
        elif assertname == '密码错误':
            assert login_page.get_login_incorrect() == 'Your email or password is incorrect!'
