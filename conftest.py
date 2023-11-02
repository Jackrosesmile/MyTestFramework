import pytest
import yaml
from src.base_layer.driver_manager import DriverManager


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests against")
    parser.addoption("--browse", action="store", default="chrome", help="Browser to use")


@pytest.fixture(scope='session')
def config(request):
    env = request.config.getoption("--env")
    browse = request.config.getoption("--browse")

    with open("src/resources/config.yaml", 'r') as f:
        config = yaml.safe_load(f)

    env_config = config['environments'].get(env)
    if not env_config:
        pytest.fail(f'Invalid environment: {env}')

    browse_config = config['browsers'].get(browse)
    if not browse_config:
        pytest.fail(f'Invalid browser: {browse}')

    return {"env": env_config, "browse": {"type": browse, "path": browse_config}}


@pytest.fixture(scope='session')
def driver_manager(config):
    driver_manager = DriverManager(config)
    driver = driver_manager.get_driver()
    driver.get(config['env'])
    yield driver
    driver.quit()
