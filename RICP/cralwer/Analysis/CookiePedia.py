#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @created by CYang on 14:15 2023/2/23 0023
# @File: CookiePedia.py
import json

import requests
from lxml import etree

def main():
    website = "www.apple.com"
    url = 'https://cookiepedia.co.uk/website/' + website
    data = {'test': 'data'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0',
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        # "Accept-Language":"en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        # "Connection":"keep-alive",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    resp = requests.get(url, headers=headers, params=data)
    html = etree.HTML(resp.text)
    # Necessary Cookies  number
    necessary = html.xpath('//*[@id="row-second"]/div/div/div[2]/div[1]/div[1]/p//text()')
    necessary[0] = "necessary_cookies"

    # Performance Cookies  number
    performance = html.xpath('//*[@id="row-second"]/div/div/div[2]/div[1]/div[2]/p//text()')
    performance[0] = "performance_cookies"

    # Functionality Cookies  number
    functionality = html.xpath('//*[@id="row-second"]/div/div/div[2]/div[1]/div[3]/p//text()')
    functionality[0] = "functionality_cookies"

    # Targeting Cookies  number
    targeting = html.xpath('//*[@id="row-second"]/div/div/div[2]/div[1]/div[4]/p//text()')
    targeting[0] = "targeting_cookies"

    # Unknown Cookies  number
    unknown = html.xpath('//*[@id="row-second"]/div/div/div[2]/div[1]/div[5]/p//text()')
    unknown[0] = "unknown_cookies"

    persistent_cookies = html.xpath('//*[@id="row-second"]/div/div/div[4]/div[1]/h2//text()')
    first_party_cookies = html.xpath('//*[@id="row-second"]/div/div/div[5]/div[1]/h2//text()')
    session_cookies = html.xpath('//*[@id="row-second"]/div/div/div[4]/div[2]/h2//text()')
    third_party_cookies = html.xpath('//*[@id="row-second"]/div/div/div[5]/div[2]/h2//text()')

    dict_all_website_cookie = {}
    dict_cookie_classifier = {}  # 存储站点对应的cookie类别及数目
    for i in range(2):
        dict_cookie_classifier[necessary[0]] = necessary[1]
        dict_cookie_classifier[performance[0]] = performance[1]
        dict_cookie_classifier[functionality[0]] = functionality[1]
        dict_cookie_classifier[targeting[0]] = targeting[1]
        dict_cookie_classifier[unknown[0]] = unknown[1]

    dict_cookie_classifier["persistent_cookies"] = persistent_cookies[0]
    dict_cookie_classifier["first_party_cookies"] = first_party_cookies[0]
    dict_cookie_classifier["session_cookies"] = session_cookies[0]
    dict_cookie_classifier["third_party_cookies"] = third_party_cookies[0]

    dict_all_website_cookie[website] = dict_cookie_classifier

    with open("cookies.json", "w") as f:
        f.write(json.dumps(dict_all_website_cookie, indent=4, ensure_ascii=False))
    print("Successfully!")


if __name__ == '__main__':
    main()