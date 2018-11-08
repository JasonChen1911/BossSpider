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
import re

class BossSpider(object):
    def get_web(self, url, referer=None):
        session = requests.session()
        if(referer):
            HEADERS['referer'] = referer
        while (True):
            try:
                response = session.get(url, headers = HEADERS)
                if response.status_code == 200:
                    return response
            except:
                pass


    def get_menu(self):
        url = 'https://www.zhipin.com/?ka=header-home-logo'
        response = self.get_web(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div_soups = soup.find_all('div', class_='menu-sub')
        a_soups = div_soups[0].find_all('a')
        for a_soup in a_soups:
            #print(a_soup['href'])
            #print(a_soup.text)
            pass
    def write_csv(self, data):
        with open('/mnt/jobs_detail.txt', 'a') as fp:
            fp.write(data+'\n')

    def get_category_info(self, category):
        base_url = 'https://www.zhipin.com'
        old_url = ''
        for index in range(1, 11):
            if index == 1:
                url = base_url + category
                self.get_web(url)
            else:
                url = base_url + category + '&page=' + str(index) + "&ka=page-" + str(index)
                self.get_web(url, old_url)
            old_url = url
            response = self.get_web(url)
            soup = BeautifulSoup(response.text, 'lxml')
            div_soup = soup.find_all('div', class_ = 'job-list')
            li_soups = div_soup[0].find_all('li')
            for li_soup in li_soups:
                data = {}
                info_soup = li_soup.find_all('div', class_='info-primary')[0]
                data['job_id'] = info_soup.find_all('a')[0]['data-jid']
                data['job_title'] = info_soup.find_all('div', class_='job-title')[0].text
                data['job_salary'] = info_soup.find_all('span')[0].text
                pattern = re.compile(r'\<p\>(.*)\<em class="vline"\>\<\/em\>(.*?)\<em class="vline"\>\<\/em\>(.*)\<\/p\>', re.S)
                info_str = str(info_soup)
                result = re.search(pattern, info_str)
                data['job_addr'] = result.group(1)
                data['job_age'] = result.group(2)
                data['job_education'] = result.group(3)
                company_soup = li_soup.find_all('div', class_='info-company')[0]
                data['company_name'] = company_soup.find_all('h3')[0].text
                pattern = re.compile(r'<p>(.*)<em class="vline"></em>(.*?)<em class="vline"></em>(.*)</p>', re.S)
                company_str = str(company_soup)
                result = re.search(pattern, company_str)
                data['company_industry'] = result.group(1)
                data['company_financing'] = result.group(2)
                data['company_size'] = result.group(3)
                str_data = data['job_id'] +'|'+ data['job_title'] +'|'+ data['job_salary'] +'|'+ data['job_addr'] +'|'+ data['job_age'] +'|'+ data['job_education'] \
                           +'|'+ data['company_name'] +'|'+ data['company_industry'] +'|'+ data['company_financing'] +'|'+ data['company_size']
                self.write_csv(str_data)





if __name__ == '__main__':
    category_list = ['/c101010100-p100101/', '/c101010100-p100102/', '/c101010100-p100103/']
    for category in category_list:
        BossSpider().get_category_info(category)



