#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2018/11/7 4:11 PM
# @Author       : JasonChen
# @File         : database_managers.py
# @Software     : PyCharm
# @description  : 数据库操作

import redis
import pymysql
from settings import *

class RedisClient(object):
    def __init__(self):
        self._db = redis.Redis(REDISHOST, REDISPORT, decode_responses=True)

    def category_put(self, database, dict_data):
        key = tuple(dict_data.keys())[0]
        value = tuple(dict_data.values())[0]
        self._db.hsetnx(database, key, value)

    def info_put(self, database, dict):
        pass




class MysqlClient(object):
    pass


if __name__ == '__main__':
    dict = {'/c101010100-p100101/':'Java'}
    RedisClient().category_put('boss_category', dict)
