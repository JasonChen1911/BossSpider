#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2018/11/7 2:48 PM
# @Author       : JasonChen
# @File         : boss_spider.py
# @Software     : PyCharm
# @description  :



import requests
from bs4 import BeautifulSoup
from settings import HEADERS

class BossSpider(object):
    def get_web(self, url):
        session = requests.session()
        response = session.get(url, headers = HEADERS)
        return response

    def get_menu(self):
        url = 'https://www.zhipin.com/?ka=header-home-logo'
        response = self.get_web(url)
        print(response)
        #print(response.text)
        soup = BeautifulSoup(response.text, 'lxml')
        div_soups = soup.find_all('div', class_='menu-sub')
        a_soups = div_soups[0].find_all('a')
        for a_soup in a_soups:
            #print(a_soup['href'])
            #print(a_soup.text)
            pass

    def get_category_info(self, category):
        base_url = 'https://www.zhipin.com'
        for index in range(1, 11):
            url = base_url + category + '&page=' + str(index)
            print(url)
        url = 'https://www.zhipin.com/c101010100-p100101/&page=11'
        reponse = self.get_web(url)
        print(reponse)






if __name__ == '__main__':
    category_list = ['/c101010100-p100101/', '/c101010100-p100102/', '/c101010100-p100103/']
    for category in category_list:
        BossSpider().get_category_info(category)




