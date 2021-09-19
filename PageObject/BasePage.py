# coding=utf-8
"""
FileName: BasePage.py
Function: This is the basies off all pages. All pages inherit from this class.
Time: 2021-07-29
Author: YangGuangjian
"""

from Common.log import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from util.readYAML import readYAMLFile


class BasePage():
    def __init__(self, driver):
        self.timeout = readYAMLFile("Config", "BasePage_config.yml")['element_wait_timeout']
        self.driver = driver
        self.driver.maximize_window()
        self.handles = {}

    def open_url(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            Logger.error("打开网页异常：", e.args, url)

    def quit(self):
        self.driver.quit()

    def _find_element(self, loc):
        # 查找元素
        print(loc)
        try:
            WebDriverWait(self.driver, self.timeout).until(lambda x: x.find_element(loc[0], loc[1]))
        except Exception as e:
            Logger.error("查找元素超时：", e.args, loc)

        try:
            return self.driver.find_element(loc[0], loc[1])
        except Exception as e:
            Logger.error("查找元素异常：", e.args, loc)

    def getText(self, loc):
        try:
            return self._find_element(loc).text
        except Exception as e:
            Logger.error("获取元素中文本异常：", e.args, loc)

    def sendKeys(self, loc, value, isClear=True):
        """
        输入文字，默认先清空，再输入。
        :param loc:
        :param value:
        :param isClear:
        :return:
        """
        if isClear:
            try:
                self._find_element(loc).clear()
            except Exception as e:
                Logger.error("输入内容前清理操作异常：", e.args)
        try:
            self._find_element(loc).send_keys(value)
        except Exception as e:
            Logger.error("输入内容操作异常：", e.args)

    def click(self, loc):
        """
        左单击
        :param loc:
        :return:
        """
        try:
            self._find_element(loc).click()
        except Exception as e:
            Logger.error("元素点击异常：", e.args, loc)

    def doubleClick(self, loc):
        """
        左双击
        :param loc:
        :return:
        """
        double = self._find_element(loc)
        try:
            ActionChains(self.driver).double_click(double).perform()
        except Exception as e:
            Logger.error("双击元素异常：", e.args, loc)

    def hover(self, loc):
        """
        鼠标悬停
        :param loc:
        :return:
        """
        el = self._find_element(loc)
        try:
            ActionChains(self.driver).move_to_element(el).perform()
        except Exception as e:
            Logger.error("鼠标悬停异常：", e.args, loc)

    def screenshot(self, IMGFilePath):
        """
        截屏
        :return:
        """
        try:
            return self.driver.save_screenshot(IMGFilePath)
        except Exception as e:
            Logger.error("截屏异常：", e.args)

    def getHandle(self, handle_name):
        """
        获取当前页面句柄，并存在字典中，key为入参handle_name
        :param handle_name:
        :return:
        """
        try:
            self.handles[handle_name] = self.driver.current_window_handle
        except Exception as e:
            Logger.error("获取页面句柄异常：", e.args, handle_name)

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
        try:
            self.driver.switch_to.window(self.handles[handle_name])
        except Exception as e:
            Logger.error("切换窗口异常：", e.args, handle_name)
