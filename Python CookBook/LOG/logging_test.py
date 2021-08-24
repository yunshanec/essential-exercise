# -*- coding: utf-8 -*-
# @Time : 2021/07/08 09:51
# @Author : yunshan
# @File : logging_test.py
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info('Start reading database')

records = [i for i in range(0,5)]
logger.debug('Records:{}'.format(records))
logger.info('Updating records ...')
logger.info('Finish updating records.')