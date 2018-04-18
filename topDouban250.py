#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv
import io
import sys

def getHtml():
    urls = []
    for i in range(0,10):
        url = 'https://book.douban.com/top250?start=%s' %(i*25)
        urls.append(url)
    return urls
def getDetails():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    headers = {"User-Agent": user_agent}
    books = []
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
    for linkNum in range(len(getHtml())):
        res = requests.get(getHtml()[linkNum],headers = headers)
        # res = res.decode('utf-8')
        soup = BeautifulSoup(res.text,'html.parser')
        items = soup.find('div',class_='indent').find_all('tr',class_='item')


        for imgNum in range(len(items)):
            book = []
            bookAlbum = items[imgNum].find('img')['src']
            book.append(bookAlbum)
            bookName = items[imgNum].find_all("a")[1].text
            book.append(bookName)
            # print(items[imgNum].find("div",class_ = "pl2").find("span",style = "font-size:12px;"))
            bookDetails = items[imgNum].find("p",class_ = "pl").text
            book.append(bookDetails)
            bookRating = items[imgNum].find("div",class_ = "star clearfix").find_all("span",class_ = "rating_nums")[0].text
            book.append(bookRating)

            # print(items[imgNum].find("div",class_ = "star clearfix").find_all("span",class_ = "pl")[0].text.split())
            try:
                bookQuote = items[imgNum].find_all("span",class_ = 'inq')[0].text

            except IndexError:
                continue
            book.append(bookQuote)
            books.append(book)
    fp = open("book-test.txt","w")
    for i in range(len(books)):
        print("第%s本书"%(i+1),books[i])

    fp.close()
    return books
getDetails()
