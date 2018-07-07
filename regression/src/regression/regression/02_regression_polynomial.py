# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


'''
    f_theta(x) = theta_0 * theta_1 * x + theta_2 * x^2 + ... + theta_n * x^n
'''

n_theta = 3

theta_orders = []
for i in range(n_theta):
    theta_orders.append(i)

theta = np.random.rand(n_theta)

# 학습 데이터.
train = np.loadtxt('./data/click.csv', delimiter=',', dtype='int', skiprows=1)
train_x = train[:,0]
train_y = train[:,1]

# 평균과 표준편차.
train_x_mean = train_x.mean()
train_x_std = train_x.std()


# z-score = (x - mean) / std
def z_score(x):
    return (x - train_x_mean) / train_x_std


train_x_z = z_score(train_x)


# np.ones(n): 1로 n개를 채운 배열.
# a = [1, 2, 3], b = [4, 5, 6] 일 때, np.vstack([a, b]) 는 [[1, 2, 3], [4, 5, 6]] 이다.
def to_matrix(x):
    stacks = []
    for n in range(n_theta):
        if (n == 0):
            stacks.append(np.ones(x.shape[0]))  # (1, 1, ..., 1)
        else:
            stacks.append(x**theta_orders[n])

    return np.vstack(stacks).T


'''
    n_train = train_x.shape[0]  # 데이터 개수.
'''


X = to_matrix(train_x_z)        # (n_train, n_theta)


# 예측함수.
def f(x):
    return np.dot(x, theta)     # (n_train, n_theta) * (n_theta,) = (n_train,)


# 오차함수(목적함수).
def E(x, y):
    return 0.5 * np.sum((y - f(x)) ** 2)


# 학습률.
eta = 1e-3

# 오차의 차이.
diff_error = 1

# 갱신횟수.
count = 0

error = E(X, train_y)

while diff_error > 1e-2:
    theta = theta - eta * np.dot(f(X) - train_y, X)

    curr_error = E(X, train_y)
    diff_error = error - curr_error
    error = curr_error

    count += 1
    
    log = '[{}] theta: {}, diff-error: {:.4f}'
    print(log.format(count, theta, diff_error))


x = np.linspace(-3, 3, 100)
plt.plot(train_x_z, train_y, 'o')
plt.plot(x, f(to_matrix(x)))
plt.show()