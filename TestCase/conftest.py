#coding=utf-8
"""
FileName: conftest.py
save all fixtrues
Time: 2021-09-18
Author: YangGuangjian
"""

import pytest
from selenium import webdriver
from PageObject.BasePage import BasePage
from util.readYAML import readYAMLFile


# 打开浏览器,返回diver,关闭浏览器
@pytest.fixture(scope='module', params=[readYAMLFile("Config", "env_config.yml")["browser"]])
def get_driver(request):

    if request.param == "Chrome":
        # 实例化一个Chrome浏览器driver,传给BasePage，获取一个BagePage对象
        driver = webdriver.Chrome()

    if request.param == "FireFox":
        # 实例化一个FireFox浏览器driver,传给BasePage，获取一个BagePage对象
        driver = webdriver.Firefox()

    # 将driver返回给调用处
    yield driver

    # 管理driver
    driver.quit()

@pytest.fixture(params=[111,222])
def demo(request):
    return request.param

@pytest.fixture()
def d(demo):
    print(demo)
    print("fixture1")