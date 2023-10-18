#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @created by CYang on 11:19 2023/6/3 0003
# @File: cookiebot.py

import json


def get_cookies_num():
    """
    获得cookie总数
    :return:
    """
    # all_cookie.json
    path = "new_training_data\\cookiebot_num_set.json"
    with open(path, "r") as f:
        row_data = json.load(f)

    # 记录cookie的总数  36803条
    count = 0
    sum_ = 0
    for key, value in row_data.items():
        sum_ += 1
        count += value["total"]
    return count, sum_


def get_classification():
    """
    获得初始化分类
    :return:
    """
    # 初始化
    result = dict()
    necessary_cookies, preferences_cookies, statistics_cookies, marketing_cookies = 0, 0, 0, 0
    # all_cookie.json
    path = "new_training_data\\cookiebot_num_set.json"
    with open(path, "r") as f:
        row_data = json.load(f)
    for key, value in row_data.items():
        necessary_cookies += value["Necessary"]
        preferences_cookies += value["Preferences"]
        statistics_cookies += value["Statistics"]
        marketing_cookies += value["Marketing"]
    result["necessary_cookies"] = necessary_cookies
    result["preferences_cookies"] = preferences_cookies
    result["statistics_cookies"] = statistics_cookies
    result["marketing_cookies"] = marketing_cookies
    return result


def get_class_cookie(cookie_class):
    """
    包含某个类的站点数: 428个
    :return:
    """
    path = "new_training_data\\cookiebot_num_set.json"
    with open(path, "r") as f:
        row_data = json.load(f)
    cookie_num = 0
    for k, v in row_data.items():
        if v[cookie_class] != 0:
            cookie_num += 1
    print("包含" + cookie_class + "类的站点数：", cookie_num)
    # 根据marketing_cookies数从高到低排序
    row_data_sort = sorted(row_data.items(), key=lambda x: int(x[1][cookie_class]), reverse=True)
    num = 20
    for k, v in row_data_sort:
        print(k, v[cookie_class])
        num -= 1
        if 0 == num:
            break
    return None


def all_cookie_is_unknown():
    """
    多少个站点中所有的cookie都是未知的
    :return:
    """
    path = "new_training_data\\cookiebot_num_set.json"
    with open(path, "r") as f:
        row_data = json.load(f)
    unknown_num = 0
    for k, v in row_data.items():
        if v["necessary_cookies"] == "0" \
                and v["performance_cookies"] == "0" \
                and v["functionality_cookies"] == "0" \
                and v["targeting_cookies"] == "0":
            unknown_num += 1
    print(unknown_num)


def target_proportion(proportion):
    """
    target类别的cookie占比超过50%的有多少个
    :return:
    """
    path = "new_training_data\\cookiebot_num_set.json"
    with open(path, "r") as f:
        row_data = json.load(f)
    count = 0
    for key, value in row_data.items():
        necessary = value["Necessary"]
        performance = value["Preferences"]
        functionality = value["Statistics"]
        targeting = value["Marketing"]
        sum_cookie = necessary + performance + functionality + targeting
        if sum_cookie != 0 and (targeting / sum_cookie) >= proportion:
            count += 1
            print(key, value)
    print(count)
    return None


def location():
    """
    服务器位置
    :return:
    """
    sum_123 = 0
    local = {}
    path = "new_training_data\\cookiebot_num_set.json"
    with open(path, "r") as f:
        row_data = json.load(f)
    for key, value in row_data.items():
        if value["regulate"] == 123:
            sum_123 += 1
        lo = value["ServerLocation"].strip()
        if lo not in local:
            local[lo] = 1
        else:
            local[lo] = local[lo] + 1
    sorted_dict = dict(sorted(local.items(), key=lambda item: item[1], reverse=True))
    # print(sorted_dict)
    print(sum_123)

    china = {}
    united_states = {}
    united_kingdom = {}
    hong_kong = {}
    netherlands = {}
    ireland = {}
    singapore = {}
    other = {}
    with open(path, "r") as f:
        row_data = json.load(f)
    for key, value in row_data.items():
        loc = value["ServerLocation"].strip()
        if loc == "China" and value["regulate"] != 0:
            if value["total"] != 0:
                china[key] = value["regulate"]
        elif loc == "United States" and value["regulate"] != 0:
            if value["total"] != 0:
                united_states[key] = value["regulate"]
        elif loc == 'United Kingdom' and value["regulate"] != 0:
            if value["total"] != 0:
                united_kingdom[key] = value["regulate"]
        elif loc == 'Hong Kong' and value["regulate"] != 0:
            if value["total"] != 0:
                hong_kong[key] = value["regulate"]
        elif loc == 'Netherlands' and value["regulate"] != 0:
            if value["total"] != 0:
                netherlands[key] = value["regulate"]
        elif loc == 'Ireland' and value["regulate"] != 0:
            if value["total"] != 0:
                ireland[key] = value["regulate"]
        elif loc == 'Singapore':
            if value["total"] != 0:
                singapore[key] = value["regulate"]
        else:
            if value["regulate"] != 0 and value["total"] != 0:
                other[key] = value["regulate"]
    print(china)
    print(united_states)
    print(united_kingdom)
    print(hong_kong)
    print(netherlands)
    print(ireland)
    print(singapore)
    print(other)
    count = 0
    for k, v in china.items():
        if v == 12:
            count += 1
    print(count)
    return None

if __name__ == '__main__':
    # num_cookies = get_cookies_num()
    # print("收集到的cookie总数和扫描的站点数", num_cookies)  # 记录cookie的总数  22492条  1010个网站

    # 每种类别cookie的数量
    # class_cookies = get_classification()
    # print(class_cookies)

    # 计算各类包含各类cookie的站点数
    # get_class_cookie("Marketing")  # 包含各类cookie的站点数145 94 72 428

    # 计算哪些站点的cookie全是unknown
    # all_cookie_is_unknown()

    # target类别数超过自身cookie总数某个百分比的站点数和占比
    # target_proportion(0)
    location()