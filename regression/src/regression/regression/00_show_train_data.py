# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 학습 데이터를 그래프로 확인한다.
train = np.loadtxt('./data/click.csv', delimiter=',', skiprows=1)

train_x = train[:,0]
train_y = train[:,1]

plt.plot(train_x, train_y, 'o')
plt.show()