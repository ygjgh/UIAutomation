#coding=utf-8
"""
FileName: UIBasicOperation.py
Function: This is the basies off all pages. All pages inherit from this class.
Time: 2021-07-29
Author: YangGuangjian
"""

from Common.log import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class UIBasicOpreation():
    def __init__(self, driver):
        self.driver = driver
        self.handles = {}

    def open_url(self, param):
        try:
            self.driver.get(param)
        except Exception as e:
            Logger.error(e.args)

    def quit(self):
        self.driver.quit()

    def _find_element(self, loc):
        # 查找元素
        print(loc)
        try:
            WebDriverWait(self.driver, 20).until(lambda x : x.find_element(loc[0], loc[1]))
            return self.driver.find_element(loc[0], loc[1])
        except Exception as e:
            Logger.error(e.args, loc[1])

    def getText(self,loc):
        return self._find_element(loc).text

    def sendKeys(self, loc, value, isClear=True):
        """
        输入文字，默认先清空，再输入。
        :param loc:
        :param value:
        :param isClear:
        :return:
        """
        if isClear:
            self._find_element(loc).clear()
        self._find_element(loc).send_keys(value)

    def click(self, loc):
        """
        左单击
        :param loc:
        :return:
        """
        self._find_element(loc).click()

    def doubleClick(self, loc):
        """
        左双击
        :param loc:
        :return:
        """
        double = self._find_element(loc)
        ActionChains(self.driver).double_click(double).perform()

    def hover(self, loc):
        """
        鼠标悬停
        :param loc:
        :return:
        """
        el = self._find_element(loc)
        ActionChains(self.driver).move_to_element(el).perform()

    def getHandle(self, handle_name):
        """
        获取当前页面句柄，并存在字典中，key为入参handle_name
        :param handle_name:
        :return:
        """
        self.handles[handle_name] = self.driver.current_window_handle

    def saveHandle(self, handle_name, handles):
        """
        保存窗口句柄
        :param handle_name:
        :param handles:
        :return:
        """
        for handle in handles:
            if handle not in self.handles:
                try:
                    self.driver.switch_to.window(handle)
                    self.handles[handle_name] = handle
                except Exception as e:
                    Logger.error(e.args, handle_name)

    def switchWindow(self, handle_name):
        """
        切换窗口，入参为句柄名称
        :param handle_name:
        :return:
        """
        self.driver.switch_to.window(self.handles[handle_name])


