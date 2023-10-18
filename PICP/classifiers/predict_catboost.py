#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @created by CYang on 11:20 2023/5/24 0024
# @File: predict_catboost.py

import catboost as catb
from scipy.sparse import csr_matrix
import numpy as np
from catboost import Pool
import matplotlib.pyplot as plt
import pickle


def predict():
    # 加载训练好的模型
    model = catb.CatBoostClassifier()
    model.load_model('D:\papercode\CookieBlock-Consent-Classifier-main\models\catbmodel_20230524_105946.cbm')

    # 加载待预测的样本数据，假设为X_pred_csr
    row = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    col = np.array([122, 1552, 1555, 1560, 1562, 1564, 1566, 1568, 1570, 1571, 1572, 1573, 1574, 1575, 1576, 1577, 1578,
                    1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1588, 1589, 1590, 1591, 1592, 1593, 1594, 1595,
                    1596, 1597, 1598, 1599, 1600, 1601, 1602, 1653, 1654, 1655, 1656, 1657, 1658, 1659, 1660, 1661, 1662,
                    1663, 1664, 1665, 1666, 1667, 1668, 1669, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 1678, 1679,
                    1680, 1681, 1682, 1683, 1684, 1685, 1687, 1688])
    data = np.array([1.0, 1.0, 5.0, 1.0, 0.9473684210526315, 1.0, 19.0, 27.0, 3.157939355321116, 0.08696227838736109,
                     -1.0, -1.0, -1.0, -1.0, 1.0, -1.0, 1799.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 19.0, 27.0,
                     -8.0, 3.0503018554349826, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0,
                     -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 1.0,
                     -1.0, -1.0, -1.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0,
                     0.9473684210526315, 1.0])
    X_pred_csr = csr_matrix((data, (row, col)))
    # 将 csr_matrix 转换为 DMatrix 类型
    dtest = Pool(data=X_pred_csr)
    # 使用训练好的模型进行预测
    pred_probabilities = model.predict(dtest, prediction_type='Probability', thread_count=-1)
    print(pred_probabilities)
    # 预测结果为概率值，您可以根据需要进行进一步处理或转换 将概率值转换为类别标签
    pred_labels = pred_probabilities.argmax(axis=1)
    # 输出预测结果
    print(pred_labels)
    print(type(model))

def mspaint():
    # 加载损失函数值列表
    with open('loss_values3.pkl', 'rb') as file:
        loss_values = pickle.load(file)

    # 绘制损失函数下降图
    plt.plot(loss_values)
    plt.xlabel('Iteration', fontsize=18)
    plt.ylabel('MultiClass', fontsize=18)
    plt.title('Loss Function', fontsize=18)

    # 设置x轴和y轴坐标轴数字的字体大小
    plt.tick_params(axis='x', labelsize=13)
    plt.tick_params(axis='y', labelsize=13)
    plt.show()


if __name__ == '__main__':
    # predict()
    # find_tree()
    mspaint()