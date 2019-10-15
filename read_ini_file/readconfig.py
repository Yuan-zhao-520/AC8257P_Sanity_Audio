# -*- coding:utf-8 -*-

import configparser
import os


# # 获取文件夹路径
# dir_path = os.path.dirname(os.path.abspath(__file__))
# # 获取文件路径
# file_path = os.path.join(dir_path, "config.ini")
#
# # 读配置文件
# cf = configparser.ConfigParser()
# cf.read(file_path)
#
# # 获取文件中所有的section
# secs = cf.sections()
# print(secs)
#
# # 获取某个section所对应的键
# options = cf.options("Mysql-Database")
# print(options)
#
# # 获取section名为Mysql-Database所对应的全部键值对
# items = cf.items("Mysql-Database")
# print(items)
#
# # 获取[Mysql-Database]中host对应的值
# host = cf.get("Mysql-Database", "host")
# print(host)

class ReadConfig:
    """定义一个读取配置文件的类"""

    def __init__(self, filepath=None):
        if filepath:
            config_path = filepath
        else:
            dir_path = os.path.dirname(os.path.abspath(__file__))
            config_path = os.path.join(dir_path, "config.ini")
            self.cf = configparser.ConfigParser()
            self.cf.read(config_path)

    def get_db(self, param):
        value = self.cf.get("Mysql-Database", param)
        return value


if __name__ == "__main__":
    test = ReadConfig()
    t = test.get_db("host")
    print(t)
