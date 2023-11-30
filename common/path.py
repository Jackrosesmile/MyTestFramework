import os
from pathlib import Path


def get_project_root(identifier, filename):
    """
    获取包含特定标识符的目录的绝对路径。

    :param filename:
    :param identifier: 用于标识目录的文件或目录名
    :return: 包含标识符的目录的绝对路径
    """
    # os.path.abspath取脚本文件的绝对路径，os.path.dirname返回父级目录，即将文件名称去掉只保留当前文件所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    while True:
        # 判断当前目录current_dir下是否存在目标identifier目录
        if os.path.exists(os.path.join(current_dir, identifier)):
            # 将当前目录与目标目录拼接成新的路径
            identifier_path = os.path.join(current_dir, identifier)
            # 返回目标文件的绝对路径
            return os.path.join(identifier_path, filename)
        # 向上遍历取父级目录
        parent_dir = os.path.dirname(current_dir)
        # 如果当前目录的父级目录等于自身，即当前目录为根结点，即没有找到目标目录，抛出异常
        if parent_dir == current_dir:
            raise FileNotFoundError(f"未找到标识文件或目录：{identifier}")
        # 将上级目录赋值给当前目录
        current_dir = parent_dir


# datas数据目录路径
datas_dir = Path(__file__).absolute().parent.parent / "TestCase"
# driver目录路径
driver_dir = Path(__file__).parent.parent / "webdriver"
# 配置目录路径
config_dir = Path(__file__).parent.parent / "config"
# log日志路径
log_path = Path(__file__).parent.parent / "outputs" / "log_files" / "UItest.log"
# 报告文件路径
report_path = Path(__file__).parent.parent / "outputs" / "report_files"
# allure报告路径
allure_path = Path(__file__).parent.parent / "outputs" / "allure_report"

