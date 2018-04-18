#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: recunfenshili.py
@time: 2017/6/1 14:52
"""

import requests
url = "https://mp.weixin.qq.com/s/FjKnAfEOnWj1_Of70XtlUg"
headers={

		  'User-Agent':'Mozilla/5.0 (Windowfous NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'


		}
res = requests.get(url,headers)
print(res.text)

if __name__ == '__main__':
    pass