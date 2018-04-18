#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def getHtml():
    novels=[]
    url = 'http://www.biquge.jp/111392_41/'
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    headers = {"User-Agent": user_agent}
    res = requests.get(url=url,headers=headers).text
    soup = BeautifulSoup(res,"lxml")
    lists = soup.find("div",id = "list").find_all("a")
    for num in range(len(lists)):
        link = lists[num]["href"]
        catalog = lists[num].text
        getContents(url+link,catalog)

def getContents(link,catalog):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    headers = {"User-Agent": user_agent}
    res = requests.get(url=link, headers=headers).text
    soup = BeautifulSoup(res, "lxml")
    content = soup.find("div",id = "content").text.replace('\xa0','')
    print(catalog)
    fp = open(r'F:/novels/%s.txt'%catalog.replace('?','').replace('*','').replace('!',''),'w')
    fp.writelines(content)



if __name__ == "__main__":
    getHtml()