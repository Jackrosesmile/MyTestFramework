import os
import shutil

from loguru import logger
from common.path import log_path, get_config_path
from common.path import allure_path
from common.path import report_path
import pytest

logger.add(sink=log_path,
           encoding="utf8",
           level="INFO",
           rotation="1 day",
           # rotation="1kb",
           compression="zip",
           retention=3)

pytest.main(["-v", "-s",
             "--alluredir=outputs/report_files",
             "--clean-alluredir"])

env_file_path = get_config_path("environment.properties")
shutil.copy(env_file_path, report_path)

cmd = f"allure generate {report_path} -o {allure_path} -c"
os.system(cmd)
