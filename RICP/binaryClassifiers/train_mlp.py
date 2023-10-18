#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @created by CYang on 20:45 2023/9/5 0005
# @File: train_mlp.py

import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

# 加载数据 0号分类器
# X_sparse = np.load('D:\\papercode\\CookieBlock-Consent-Classifier-main\\BinaryClassifier\\sparse\\processed_20230905_171509.sparse',
#                    allow_pickle=True)
# y = np.load('D:\\papercode\\CookieBlock-Consent-Classifier-main\\BinaryClassifier\\sparse\\processed_20230905_171509.sparse.labels',
#             allow_pickle=True)

# # 加载数据 1号分类器
# X_sparse = np.load('D:\\papercode\\CookieBlock-Consent-Classifier-main\\BinaryClassifier\\sparse\\processed_20230905_171704.sparse',
#                    allow_pickle=True)
# y = np.load('D:\\papercode\\CookieBlock-Consent-Classifier-main\\BinaryClassifier\\sparse\\processed_20230905_171704.sparse.labels',
#             allow_pickle=True)

# 加载数据 2号分类器
X_sparse = np.load('..\\BinaryClassifier\\sparse\\processed_20230905_171756.sparse',
                   allow_pickle=True)
y = np.load('..\\BinaryClassifier\\sparse\\processed_20230905_171756.sparse.labels',
            allow_pickle=True)

# # 加载数据 3号分类器
# X_sparse = np.load('D:\\papercode\\CookieBlock-Consent-Classifier-main\\BinaryClassifier\\sparse\\processed_20230905_171855.sparse',
#                    allow_pickle=True)
# y = np.load('D:\\papercode\\CookieBlock-Consent-Classifier-main\\BinaryClassifier\\sparse\\processed_20230905_171855.sparse.labels',
#             allow_pickle=True)

# 转换X_sparse为NumPy密集数组
X_numpy = X_sparse

# 转换y为NumPy数组
y_numpy = np.array(y)

# 划分训练集和验证集
X_train, X_val, y_train, y_val = train_test_split(X_numpy, y_numpy, test_size=0.2, random_state=42)


# MLP模型
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dropout(0.4),  # Dropout层
    # tf.keras.layers.Dense(32, activation='relu'),  # 第二层，使用ReLU激活函数
    tf.keras.layers.Dropout(0.4),  # Dropout层
    tf.keras.layers.Dense(64, activation='relu'),  # 第三层，使用ReLU激活函数
    tf.keras.layers.Dense(1, activation='sigmoid')  # 二分类输出层
])

# 编译
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0005),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 训练
history = model.fit(X_train, y_train, epochs=100, batch_size=10, validation_data=(X_val, y_val))

# 预测
y_pred = model.predict(X_val)
y_pred_binary = (y_pred > 0.5).astype(int)

for i in range(len(y_val)):
    print(f"样本 {i + 1}: 真实标签={y_val[i]}, 预测标签={y_pred_binary[i][0]}")

