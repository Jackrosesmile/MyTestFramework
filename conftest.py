import allure
import pytest
import platform
from .business_page.home_page import HomePage
from .business_page.login_page import LoginPage
from common.driver_manager import DriverManager
from common.file_handler import read_yaml
from common.path import get_project_root, get_config_path


def pytest_addoption(parser):
    # 添加一个命令行选项 --env，用于指定测试环境，默认值为 dev
    parser.addoption("--env", action="store", default="dev", choices=['dev', 'sit', 'prod'],
                     help="命令行参数 '--env' 设置环境切换")
    # 添加一个命令行选项 --browse，用于指定使用的浏览器，默认值为 chrome
    parser.addoption("--browse", action="store", default="edge",
                     choices=['chrome', 'edge', 'firefox', 'safari'], help="命令行参数 '--browse' 设置浏览器切换")


@pytest.fixture(scope='session')
def config(request):
    # 获取环境参数
    env = request.config.getoption("--env")
    # 获取浏览参数
    browse = request.config.getoption("--browse")
    # 读取配置文件
    config_path = get_project_root('config_file', 'config.yaml')
    config = read_yaml(config_path)
    # 获取环境配置
    url = config['environments'][f'{env}'].get('url')
    # 如果环境配置不存在，则返回错误信息并停止测试
    if not url:
        pytest.fail(f'不存在的测试环境: {env}')

    # 获取浏览器配置
    browse_config = config['browsers'].get(browse)
    # 如果浏览器配置不存在，则返回错误信息并停止测试
    if not browse_config:
        pytest.fail(f'不存在的浏览器: {browse}')

    # 获取用户名和密码
    username = config['environments'][f'{env}'].get('username')
    password = config['environments'][f'{env}'].get('password')

    if not username:
        pytest.fail('用户名不存在')

    if not password:
        pytest.fail('密码不存在')

    # 返回配置信息
    return {"env": env, "url": url, "username": username, "password": password,
            "browse": {"type": browse, "path": browse_config['webdriver'], "binary_path": browse_config['binary_path']}}


driver = None


@pytest.fixture(scope='function')
def driver_manager(config):
    global driver
    # 创建一个 DriverManager 对象，并传入配置参数
    driver_manager = DriverManager(config)
    # 从 DriverManager 对象中获取 WebDriver 对象
    driver = driver_manager.get_driver()
    # 使用 WebDriver 对象打开配置中的环境 URL
    # driver.get(config['env'])
    driver.maximize_window()
    generate_environment_file(driver, config)
    yield driver
    # 退出 WebDriver 对象
    driver.quit()


@pytest.fixture(scope='function')
def init_login(driver_manager, config):
    username = config['username']
    password = config['password']
    driver_manager.get(config['url'])
    login = LoginPage(driver_manager)
    home_page = HomePage(driver_manager)
    home_page.click_login()
    login.input_username(username)
    login.input_password(password)
    login.click_login_button()
    yield driver_manager


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    global driver
    # 获取测试用例执行结果-yield（pytest内置变量）
    out_come = yield
    res = out_come.get_result()
    # 监听到失败的情况
    if res.failed:
        # 获取失败截图
        # attach这个函数需要传递三个参数，第一个：二进制数据 第二个：附件的名字  第三个：附件类型
        allure.attach(driver.get_screenshot_as_png(), '失败截图', allure.attachment_type.PNG)


def generate_environment_file(driver, config):
    browser_version = driver.execute_script("return navigator.userAgent;")
    os_info = platform.system() + " " + platform.version()
    file_path = get_config_path("environment.properties")
    with open(str(file_path), "w") as file:
        file.write(f"Browser={browser_version}\n")
        file.write(f"Operating.System={os_info}\n")
        file.write(f"Environment={config['env'].upper()},URL={config['url']}\n")
        # 添加其他需要的环境信息

# 使用 PyTest 的钩子函数在测试会话开始时生成环境信息
# @pytest.hookimpl(tryfirst=True)
# def pytest_sessionstart(session):
#     # 临时获取 WebDriver 实例
#     global driver
#     # 生成环境信息文件
#     generate_environment_file(driver)