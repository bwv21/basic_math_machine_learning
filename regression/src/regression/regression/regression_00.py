# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


'''
    매개변수가 두 개(theta0, theta1)인 경우.
'''


# 학습 데이터.
train = np.loadtxt('click.csv', delimiter=',', dtype='int', skiprows=1)
train_x = train[:,0]
train_y = train[:,1]

# 평균과 표준편차.
train_x_mean = train_x.mean()
train_x_std = train_x.std()

# z-score = (x - mean) / std
def z_score(x):
    return (x - train_x_mean) / train_x_std


train_x_z = z_score(train_x)


# 데이터 확인.
'''
plt.plot(train_x_z, train_y, 'o')
plt.show()
'''


# 예측함수.
def f(x):
    return theta_0 + theta_1 * x


# 오차함수(목적함수).
def E(x, y):
    return 0.5 * np.sum((y - f(x)) ** 2)


# 두 개의 매개변수.
theta_0 = np.random.rand()
theta_1 = np.random.rand()

# 학습률.
eta = 1e-3

# 오차의 차이.
diff_error = 1

# 갱신횟수.
count = 0

error = E(train_x_z, train_y)

while diff_error > 1e-2:
    # theta0 := theta0 - eta * sigma(f(x) - y)
    tmp_theta_0 = theta_0 - eta * np.sum(f(train_x_z) - train_y)
    
    # theta1 := theta1 - eta * sigma((f(x) - y) * x)
    tmp_theta_1 = theta_1 - eta * np.sum((f(train_x_z) - train_y) * train_x_z)

    # 매개변수의 갱신은 동시에 일어나야 함에 유의한다(tmp_ 사용하고 한 번에 업데이트).
    theta_0 = tmp_theta_0
    theta_1 = tmp_theta_1

    curr_error = E(train_x_z, train_y)
    diff_error = error - curr_error
    error = curr_error

    count += 1

    log = '[{}] theta0: {:.3f}, theta1: {:.3f}, diff-error: {:.4f}'
    print(log.format(count, theta_0, theta_1, diff_error))


# 그래프로 나타낸다
plt.plot(train_x_z, train_y, 'o')
x = np.linspace(-3, 3, 100)
plt.plot(x, f(x))
plt.show()