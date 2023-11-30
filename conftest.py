import pytest
from common.driver_manager import DriverManager
from common.file_handler import read_yaml
from common.path import get_project_root


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
    env_config = config['environments'].get(env)
    # 如果环境配置不存在，则返回错误信息并停止测试
    if not env_config:
        pytest.fail(f'不存在的测试环境: {env}')

    # 获取浏览器配置
    browse_config = config['browsers'].get(browse)
    # 如果浏览器配置不存在，则返回错误信息并停止测试
    if not browse_config:
        pytest.fail(f'不存在的浏览器: {browse}')

    # 返回配置信息
    return {"env": env_config,
            "browse": {"type": browse, "path": browse_config['webdriver'], "binary_path": browse_config['binary_path']}}


driver = None


@pytest.fixture(scope='session')
def driver_manager(config):
    global driver
    # 创建一个 DriverManager 对象，并传入配置参数
    driver_manager = DriverManager(config)
    # 从 DriverManager 对象中获取 WebDriver 对象
    driver = driver_manager.get_driver()
    # 使用 WebDriver 对象打开配置中的环境 URL
    # driver.get(config['env'])
    driver.maximize_window()
    yield driver
    # 退出 WebDriver 对象
    driver.quit()
