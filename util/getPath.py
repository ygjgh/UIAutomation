#coding=utf-8
"""
FileName: getPath.py
Function: Get the path of the project.
Time: 2021-07-28
Author: YangGuangjian
"""
import os.path

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def filePath(path, file_name):
    return os.path.join(BASE_PATH, path, file_name)

def basePath():
    return BASE_PATH

if __name__ == '__main__':
    file = filePath('config', 'log_config.yml')
    print(file)