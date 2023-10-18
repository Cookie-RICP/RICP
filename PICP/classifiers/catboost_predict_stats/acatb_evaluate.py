#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @created by CYang on 16:22 2023/6/14 0014
# @File: acatb_evaluate.py


import csv

import pandas as pd
from sklearn.metrics import accuracy_score

# 读取包含标签值和概率分布的CSV文件
data = pd.read_csv('softprob_predictions_20230308_194859.csv')

# 提取真实标签值
true_labels = data['labels']

# 根据概率分布得到预测的标签值
predicted_labels = data[['necessary', 'functional', 'analytics', 'advertising']].idxmax(axis=1)
predicted_labels = predicted_labels.map({'necessary': 0, 'functional': 1, 'analytics': 2, 'advertising': 3})

# 计算准确率
accuracy = accuracy_score(true_labels, predicted_labels)

# 打印准确率
print(f"模型的准确率为: {accuracy}")


# 加载CSV文件内容到数据结构中
with open('softprob_predictions_20230308_194859.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# 统计良性cookie和商业追踪cookie之前的误判
count1 = 0  # 将良性cookie误判为商业cookie数
count2 = 0  # 将商业cookie误判为良性cookie数
count_0_2 = 0  # 将0误判为2的数量
count_0_3 = 0  # 将0误判为3的数量
count_1_2 = 0  # 将1误判为2的数量
count_1_3 = 0  # 将1误判为3的数量

count_2_0 = 0  # 将2误判为0的数量
count_2_1 = 0  # 将2误判为1的数量
count_3_0 = 0  # 将3误判为0的数量
count_3_1 = 0  # 将3误判为1的数量

err = 0  # 全部误判数
list1 = []
list2 = []
for row in data[1:]:  # 从第二行开始循环
    true_label = int(row[0])
    predicted_label = row[1:].index(max(row[1:]))  # 获取最大概率对应的索引
    if (true_label == 0 or true_label == 1) and (predicted_label == 2 or predicted_label == 3):
        list1.append(row)
        count1 += 1
        if true_label == 0 and predicted_label == 2:
            count_0_2 += 1
        if true_label == 0 and predicted_label == 3:
            count_0_3 += 1
        if true_label == 1 and predicted_label == 2:
            count_1_2 += 1
        if true_label == 1 and predicted_label == 3:
            count_1_3 += 1
    if (true_label == 2 or true_label == 3) and (predicted_label == 0 or predicted_label == 1):
        list2.append(row)
        count2 += 1
        if true_label == 2 and predicted_label == 0:
            count_2_0 += 1
        if true_label == 2 and predicted_label == 1:
            count_2_1 += 1
        if true_label == 3 and predicted_label == 0:
            count_3_0 += 1
        if true_label == 3 and predicted_label == 1:
            count_3_1 += 1
    if true_label != predicted_label:
        err += 1
print("将真良性cookie误判为商业跟踪cookie的数量：", count1)
print("0 -> 2:", count_0_2)
print("0 -> 3:", count_0_3)
print("1 -> 2:", count_1_2)
print("1 -> 3:", count_1_3)
print("========================")
print("将商业跟踪cookie的数量误判为良性cookied的数量：", count2)
print("2 -> 0:", count_2_0)
print("2 -> 1:", count_2_1)
print("3 -> 0:", count_3_0)
print("3 -> 1:", count_3_1)
print("========================")
print(f"模型的严重误判率为: ",  (count1 + count2) / 409)
print(f"模型的全部误判数: ",  err)
print("========================")
print(list1)
print(list2)