#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @created by CYang on 17:31 2023/9/5 0005
# @File: train_cnn.py

import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

# 加载数据
X_sparse = np.load('/BinaryClassifier\\sparse\\processed_20230905_171509.sparse',
                   allow_pickle=True)
y = np.load('/BinaryClassifier\\sparse\\processed_20230905_171509.sparse.labels',
            allow_pickle=True)

# 转换X_sparse为NumPy数组
X_numpy = np.array(X_sparse)

# 转换y为NumPy数组
y_numpy = np.array(y)

# 划分训练集和验证集
X_train, X_val, y_train, y_val = train_test_split(X_numpy, y_numpy, test_size=0.2, random_state=42)

# 构建CNN模型
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')  # 二分类输出层
])

# 编译模型
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 训练模型
history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))




