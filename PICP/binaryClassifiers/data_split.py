#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @created by CYang on 10:16 2023/9/5 0005
# @File: data_split.py

import copy
import json
import random

json_file_path = 'D:\\papercode\\CookieBlock-Consent-Classifier-main\\training_data\\example_crawl_20210213_153228.json'

dict_0 = {}
dict_1 = {}
dict_2 = {}
dict_3 = {}

# 加载全部数据
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
print(len(data))
# 数据集划分为四类
for key, value in data.items():
    if 0 == value["label"]:
        # 置1
        temp = copy.copy(value)
        temp["label"] = 1
        dict_0[key] = temp
    elif 1 == value["label"]:
        # 置1
        temp = copy.copy(value)
        temp["label"] = 1
        dict_1[key] = temp
    elif 2 == value["label"]:
        # 置1
        temp = copy.copy(value)
        temp["label"] = 1
        dict_2[key] = temp
    elif 3 == value["label"]:
        # 置1
        temp = copy.copy(value)
        temp["label"] = 1
        dict_3[key] = value

# 向四种数据集中加入数量相同的随机选取的其它类型样本
num_0, num_1, num_2, num_3 = len(dict_0), len(dict_1), len(dict_2), len(dict_3)
print(len(dict_0), len(dict_1), len(dict_2), len(dict_3))

# 查找标签不是0的样本
count = 0
for key, value in data.items():
    if count == 578:
        break
    if value["label"] != 0:
        temp = copy.copy(value)
        temp["label"] = 0
        dict_0[key] = temp
        count += 1

# 查找标签不是1的样本
count = 0
for key, value in data.items():
    if count == 162:
        break
    if value["label"] != 1:
        temp = copy.copy(value)
        temp["label"] = 0
        dict_1[key] = temp
        count += 1

# 查找标签不是2的样本
count = 0
for key, value in data.items():
    if count == 628:
        break
    if value["label"] != 2:
        temp = copy.copy(value)
        temp["label"] = 0
        dict_2[key] = temp
        count += 1

# 查找标签不是3的样本
count = 0
for key, value in data.items():
    if count == 820:
        break
    if value["label"] != 3:
        temp = copy.copy(value)
        temp["label"] = 0
        dict_3[key] = temp
        count += 1

# 划分完成
json_file_path = 'dict_0.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(dict_0, json_file, ensure_ascii=False, indent=4)
json_file_path = 'dict_1.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(dict_1, json_file, ensure_ascii=False, indent=4)
json_file_path = 'dict_2.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(dict_2, json_file, ensure_ascii=False, indent=4)
json_file_path = 'dict_3.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(dict_3, json_file, ensure_ascii=False, indent=4)

print(len(dict_0), len(dict_1), len(dict_2), len(dict_3))





