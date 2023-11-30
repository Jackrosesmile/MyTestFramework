import os
from loguru import logger
from src.common.path import log_path
from src.common.path import allure_path
from src.common.path import report_path
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

cmd = f"allure generate {report_path} -o {allure_path} -c"
os.system(cmd)
