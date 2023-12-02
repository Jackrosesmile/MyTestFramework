import platform
import pytest


def generate_environment(config, driver_manager):
    browser_version = driver_manager.execute_script("return navigator.userAgent;")
    os_info = platform.system() + " " + platform.release()

    with open("environment.properties", "w") as file:
        file.write(f"Browser={browser_version}\n")
        file.write(f"Operating.System={os_info}\n")
        # 添加其他需要的环境信息
