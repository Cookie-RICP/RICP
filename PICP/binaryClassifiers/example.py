#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @created by CYang on 14:04 2023/9/5 0005
# @File: example.py

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 加载示例数据集，这里使用的是鸢尾花数据集
data = datasets.load_iris()
X = data.data
y = (data.target == 0).astype(int)  # 将鸢尾花种类为0的样本标记为正类，其余为负类

# 将数据集分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建SVM模型
svm_model = SVC(kernel='linear', C=1.0)

# 训练模型
svm_model.fit(X_train, y_train)

# 进行预测
y_pred = svm_model.predict(X_test)

# 计算准确度
accuracy = accuracy_score(y_test, y_pred)
print(f"模型准确度：{accuracy:.2f}")
