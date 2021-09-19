#coding=utf-8
"""
FileName: log.py
Function: config log.
Time: 2021-07-29
Author: YangGuangjian
"""

import time
import logging.config
from util.readYAML import readYAML
from util.getPath import filePath


log_config = readYAML('config', 'log_config.yml')
log_config['handlers']['info_file_handler']['filename'] = filePath('Logs', time.strftime("%Y%m%d")+'.log')
log_config['handlers']['error_file_handler']['filename'] = filePath('Logs', 'error_'+time.strftime("%Y%m%d")+'.log')


class Logger():
    def __init__(self):
        logging.config.dictConfig(log_config)
        self.Logger = logging.getLogger('root')

Logger = Logger().Logger



if __name__ == '__main__':
    Logger.info('info')
    Logger.error('error')