#coding=utf-8
"""
FileName: conftest.py
save all fixtrues
Time: 2021-09-18
Author: YangGuangjian
"""

import pytest
from selenium import webdriver
from Common.UIBasicOperation import UIBasicOpreation


# 打开浏览器,返回diver,关闭浏览器
@pytest.fixture(scope='module')
def get_driver():

    # 实例化一个driver
    driver = UIBasicOpreation(webdriver.Firefox())

    # 将driver返回给调用处
    yield driver

    # 管理driver
    driver.quit()

