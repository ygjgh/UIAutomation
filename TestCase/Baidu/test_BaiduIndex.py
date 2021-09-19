# coding=utf-8
"""
FileName: test_BaiduIndex.py
This is the test cases of Baidu IndexPage.
Time: 2021-09-19
Author: YangGuangjian
"""

import time
import pytest
from Common.log import Logger
from PageObject.BaiduIndexPage import BaiduPage
from util.getPath import filePath


class TestBaiduIndex():

    @pytest.mark.baiduIndexPage
    def test_search(self, get_driver):
        bp = BaiduPage(get_driver)
        bp.open_url("http://www.baidu.com")
        bp.search_box_input("python")
        bp.baidu_button_click()
        time.sleep(3)
        try:
            assert 1 == 2
        except Exception as e:
            bp.screenshot(filePath('IMGFiles\BaiduIndex', "index.png"))
            Logger.info("截取百度首页")
            raise


if __name__ == '__main__':
    pytest.main(['test_BaiduIndex.py', '-s'])
