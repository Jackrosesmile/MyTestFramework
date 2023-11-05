import os


def get_project_root(identifier, filename):
    """
    获取包含特定标识符的目录的绝对路径。

    :param filename:
    :param identifier: 用于标识目录的文件或目录名
    :return: 包含标识符的目录的绝对路径
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.exists(os.path.join(current_dir, identifier)):
            identifier_path = os.path.join(current_dir, identifier)
            return os.path.join(identifier_path, filename)
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:
            raise FileNotFoundError(f"未找到标识文件或目录：{identifier}")
        current_dir = parent_dir
