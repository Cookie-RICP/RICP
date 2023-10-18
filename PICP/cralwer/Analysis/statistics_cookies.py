#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @created by CYang on 8:40 2023/2/28 0028
# @File: statistics_cookies.py
import json


def get_cookies_num():
    """
    获得cookie总数
    :return:
    """
    # all_cookie.json
    path = "all_cookie.json"
    with open(path, "r") as f:
        row_data = json.load(f)

    # 记录cookie的总数  36803条
    count = 0
    sum_ = 0
    for key, value in row_data.items():
        sum_ += 1
        count += int(value["necessary_cookies"]) \
                 + int(value["performance_cookies"]) \
                 + int(value["functionality_cookies"]) \
                 + int(value["targeting_cookies"]) \
                 + int(value["unknown_cookies"])
    return count, sum_


def get_classification():
    """
    获得初始化分类
    :return:
    """
    # 初始化
    result = dict()
    necessary_cookies, performance_cookies, functionality_cookies, targeting_cookies, unknown_cookies = 0, 0, 0, 0, 0

    persistent_cookies = 0
    first_party_cookies = 0
    session_cookies = 0
    third_party_cookies = 0
    # all_cookie.json
    path = "all_cookie.json"
    with open(path, "r") as f:
        row_data = json.load(f)
    for key, value in row_data.items():
        necessary_cookies += int(value["necessary_cookies"])
        performance_cookies += int(value["performance_cookies"])
        functionality_cookies += int(value["functionality_cookies"])
        targeting_cookies += int(value["targeting_cookies"])
        unknown_cookies += int(value["unknown_cookies"])
        persistent_cookies += int(value["persistent_cookies"])
        first_party_cookies += int(value["first_party_cookies"])
        session_cookies += int(value["session_cookies"])
        third_party_cookies += int(value["third_party_cookies"])
    # result["necessary_cookies"] = necessary_cookies
    # result["performance_cookies"] = performance_cookies
    # result["functionality_cookies"] = functionality_cookies
    # result["targeting_cookies"] = targeting_cookies
    result["unknown_cookies"] = unknown_cookies
    result["persistent_cookies"] = persistent_cookies
    result["first_party_cookies"] = first_party_cookies
    result["session_cookies"] = session_cookies
    result["third_party_cookies"] = third_party_cookies
    return result


def get_class_cookie(cookie_class):
    """
    包含某个类的站点数: 428个
    :return:
    """
    path = "all_cookie.json"
    with open(path, "r") as f:
        row_data = json.load(f)
    cookie_num = 0
    for k, v in row_data.items():
        if v[cookie_class] != '0':
            cookie_num += 1
    print("包含" + cookie_class + "类的站点数：", cookie_num)
    # 根据target_cookies数从高到低排序
    row_data_sort = sorted(row_data.items(), key=lambda x: int(x[1][cookie_class]), reverse=True)
    num = 100
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
    path = "all_cookie.json"
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
    path = "all_cookie.json"
    with open(path, "r") as f:
        row_data = json.load(f)
    count = 0
    for key, value in row_data.items():
        necessary = int(value["necessary_cookies"])
        performance = int(value["performance_cookies"])
        functionality = int(value["functionality_cookies"])
        targeting = int(value["targeting_cookies"])
        unknow = int(value["unknown_cookies"])
        third = int(value["third_party_cookies"])
        sum_cookie = necessary + performance + functionality + targeting + unknow
        if sum_cookie != 0 and (third / sum_cookie) >= proportion:
            count += 1
            print(key, value)
    print(count)
    return None


if __name__ == '__main__':
    # num_cookies = get_cookies_num()  # type(row_data)) == dict  len(row_data) == 1007
    # print("记录的cookie条目数：", num_cookies)  # 记录cookie的总数  36803条

    # 计算每种cookie的数量
    class_cookies = get_classification()
    print(class_cookies)

    # 计算各类包含各类cookie的站点数
    # get_class_cookie("targeting_cookies")  # 包含各类cookie的站点数145 94 72 428

    # 计算哪些站点的cookie全是unknown
    # all_cookie_is_unknown()

    # target类别数超过自身cookie总数某个百分比的站点数和占比
    # target_proportion(0.8)