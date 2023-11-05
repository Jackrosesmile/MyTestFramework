import pytest
import logging
import os
from src.base_layer.driver_manager import DriverManager
from src.utils_layer.file_handler import read_yaml
from src.utils_layer.construct_full_path import get_project_root
from _pytest.logging import LogCaptureFixture


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests against")
    parser.addoption("--browse", action="store", default="chrome", help="Browser to use")


@pytest.fixture(scope='session')
def config(request):
    env = request.config.getoption("--env")
    browse = request.config.getoption("--browse")

    config = read_yaml("src/resources/config.yaml")

    env_config = config['environments'].get(env)
    if not env_config:
        pytest.fail(f'Invalid environment: {env}')

    browse_config = config['browsers'].get(browse)
    if not browse_config:
        pytest.fail(f'Invalid browser: {browse}')

    return {"env": env_config,
            "browse": {"type": browse, "path": browse_config['webdriver'], "binary_path": browse_config['binary_path']}}


@pytest.fixture(scope='session')
def driver_manager(config):
    driver_manager = DriverManager(config)
    driver = driver_manager.get_driver()
    driver.get(config['env'])
    yield driver
    driver.quit()
