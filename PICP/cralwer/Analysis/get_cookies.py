#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @created by CYang on 9:12 2023/3/3 0003
# @File: get_cookies.py

import requests

url = "www.163.com"
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'
    }


# 替换为你要获取cookie的网站URL
response = requests.get(url, headers=headers)
cookies = response.cookies  # 获取响应中的所有cookie
for cookie in cookies:
    print(cookie.name, cookie.value)