#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @created by CYang on 9:32 2023/9/5 0005
# @File: train_svc.py

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, classification_report
import numpy as np
from tqdm import tqdm

# 加载数据
X_sparse = np.load('/BinaryClassifier\\sparse\\processed_20230905_171509.sparse',
                   allow_pickle=True)
y = np.load('/BinaryClassifier\\sparse\\processed_20230905_171509.sparse.labels',
            allow_pickle=True)

# 将数据集分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_sparse, y, test_size=0.2, random_state=45)

# 核函数rbf/poly
svm_model = SVC(kernel='poly', C=1.0)  # rbf poly

svm_model.fit(X_train, y_train)

# 预测
y_pred = svm_model.predict(X_test)

# 计算准确度
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# 计算精确度
precision = precision_score(y_test, y_pred)
print(f"Precision: {precision:.2f}")

# 计算召回率
recall = recall_score(y_test, y_pred)
print(f"Recall: {recall:.2f}")

# 计算F1分数
f1 = f1_score(y_test, y_pred)
print(f"F1 Score: {f1:.2f}")

# 计算ROC AUC
roc_auc = roc_auc_score(y_test, y_pred)
print(f"ROC AUC: {roc_auc:.2f}")

# 计算混淆矩阵
confusion = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(confusion)

# 输出分类报告
report = classification_report(y_test, y_pred)
print("Classification Report:")
print(report)

'''
classifiers = []
y_train = np.array(y_train)
# 训练分类器
for class_label in range(4):
    # 然后进行类型转换
    y_binary = (y_train == class_label).astype(int)
    svm_model = SVC(kernel='linear', C=1.0)
    svm_model.fit(X_train, y_binary)
    classifiers.append(svm_model)

# 进行预测
predictions = np.zeros((X_test.shape[0], 4))
for class_label in range(4):
    prediction = classifiers[class_label].decision_function(X_test)
    predictions[:, class_label] = prediction

# 最终预测为具有最高得分的类别
final_predictions = np.argmax(predictions, axis=1)
accuracy = accuracy_score(y_test, final_predictions)

# 打印模型的准确率
print(f"模型准确率：{accuracy:.2f}")
'''




