#coding=utf-8
"""
FileName: BaiduIndexPage.py
All elements of Baidu IndexPage and element functions.
Time: 2021-09-19
Author: YangGuangjian
"""

from PageObject.BasePage import BasePage
from Locator.BaiduIndexLocations import IndexPageLocator as IPL #导入百度首页元素定位类

class BaiduPage(BasePage):
    def __init__(self, driver):
        super(BaiduPage, self).__init__(driver)

    # 在Baidu首页搜索框内输入内容
    def search_box_input(self, comment):
        self.sendKeys(IPL.INPUT_WD, comment)

    # 点击”百度一下“按钮
    def baidu_button_click(self):
        self.click(IPL.BUTTON_SEARCH)

