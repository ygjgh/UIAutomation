# coding=utf-8
import time
import pytest
from Common.log import Logger
from util import readYAML
from Locator.indexPage import IndexPageLocator as ipl


class TestBaiduIndex():
    def test_baidu_index(self, get_driver):
        print("执行test1")
        get_driver.open_url("https://www.baidu.com")
        Logger.info("打开浏览器")
        get_driver.sendKeys(ipl.INPUT_WD,"python")
        get_driver.click(ipl.BUTTON_SEARCH)
        time.sleep(3)



if __name__ == '__main__':
    pytest.main(['test_index.py', '-s'])
