#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
url = 'https://www.zhihu.com/question/23252065'
headers = {
           "Connection":'keep-alive',
           "Cookie":'_zap=cc4069aa-4cf0-49d3-a851-e2558bf9d0e4; aliyungf_tc=AQAAABRGrkfRFQgA7q8BJGy5PdEzOSsW; _xsrf=fa27f801-8a9f-4cf6-aec1-d2da68584786; q_c1=d1dc494fd6834f87ae31f01b7c05bef2|1519827971000|1515555576000; capsion_ticket="2|1:0|10:1519827975|14:capsion_ticket|44:NWIzZmMwZDExZGZhNDQ1MWJjMmM5YTYwNzBjYWVkYjE=|5c5081d12aab259433965a10473c324ceb552bf80a56dcb4cca0163785e0348b"; z_c0="2|1:0|10:1519827976|4:z_c0|80:MS4xNUNsT0FBQUFBQUFtQUFBQVlBSlZUUWdLaEZza1M0RDBkaWVvY3A2TU1sNFlPZGtJRW5LdDZRPT0=|31cb07f7c9318bd58f2ba397583a1d1275af1c484a7b51f0f724cb34dfbc3d8f"; d_c0="AFCsI4dINw2PTh1tSZlhIhWWLYg9lSdVsZQ=|1519828299"',
           'Host': 'www.zhihu.com',
           'Referer': 'https://www.zhihu.com/',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
           }
res = requests.get(url=url,headers=headers).text
soup = BeautifulSoup(res,'lxml').find("div",class_ = "QuestionPage")
print(soup)