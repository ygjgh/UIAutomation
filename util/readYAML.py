#coding=utf-8
"""
FileName: readYAML.py
Function: Read info from YAML file.
Time: 2021-07-29
Author: YangGuangjian
"""

import yaml
from util.getPath import filePath


def readYAMLFile(path, file_name):
    """
    read yaml-file
    :param path: the path of yaml-file
    :param file_name: the name of yaml-file
    :return: data of yaml-file
    """
    file_path = filePath(path, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.load(f, Loader=yaml.FullLoader)