#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @created by CYang on 15:54 2023/6/18 0018
# @File: importance.py


import numpy as np

# # 从CSV文件读取内容
# data = np.genfromtxt('feature_importance.csv', delimiter=',')
#
# sum_ = 0
# # 遍历数组
# i = 1051
# while i < 1551:
#     # 在这里处理每一行的数据
#     sum_ += data[i]
#     print(data[i])
#     i += 1
# print("sum:", sum_)

list_importance = [12, 10.7, 10.6, 6.7, 5.8, 4.8, 4.2, 3.5, 2.9, 2.7]
list_name = ["sameSite", "CookieNameToken", "hostOnly", "expiry", "CookieNameTop", "session", "domain.", "jsContent", "alphaContent", "isIdentifier"]
