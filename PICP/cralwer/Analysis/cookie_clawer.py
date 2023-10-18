#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @created by CYang on 15:40 2023/3/27 0027
# @File: cookie_clawer.py

import requests

url = "https://www.baidu.com"

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0',
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        # "Accept-Language":"en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        # "Connection":"keep-alive",
        "Content-Type": "application/x-www-form-urlencoded"
    }
response = requests.get(url, headers=headers)

cookies = response.cookies

for cookie in cookies:
    print(cookie.name, cookie.value, cookie.domain, cookie.path, cookie.expires, cookie.secure)

