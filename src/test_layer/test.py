from src.utils_layer.construct_full_path import get_project_root
import logging
import os


log_file_path = get_project_root('resources', 'execution.log')
    # # 如果日志目录不存在，则创建该目录
if not os.path.exists(log_file_path):
    print('日志路径不存在')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=log_file_path,  # 日志文件名
                    filemode='a')  # 'a'表示追加模式，'w'表示写入模式
    # 记录日志配置启动的消息
logging.info("Logging setup is completed.")