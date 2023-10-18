#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @created by CYang on 16:35 2023/9/5 0005
# @File: test.py

import copy

data = {
    "a": {
        "label": 1
    }
}

dict_0 = {}
for key, value in data.items():
    if value["label"] != 0:
        temp = copy.copy(value)
        temp["label"] = 0
        dict_0[key] = temp

print(data)   # 原始的data字典保持不变
print(dict_0)  # 包含修改后的键-值对的新字典dict_0