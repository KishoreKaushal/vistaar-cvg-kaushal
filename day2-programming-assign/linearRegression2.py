#!/usr/bin/python3

import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

fname = 'dat2.txt'
data = np.loadtxt(fname)
y = data[:]
x = np.arange(1,len(data)+1)

n = int(len(x))
sum_xi = x.sum()
sum_xi_sqr = np.square(x).sum()
sum_yi = y.sum()
sum_xi_yi = (x*y).sum()

weights = np.array([0 , 0])


A = np.array([[n, sum_xi], [sum_xi , sum_xi_sqr]])
B = np.array([sum_yi , sum_xi_yi])
inv_matrices = inv(A)
weights = inv_matrices.dot(B)
[c , m ] = weights
# y = mx + c
print("SLOPE: ", m, "INTERCEPT: ", c)

X = np.array([np.min(x), np.max(x)])
Y = np.zeros(X.shape)
Y[0] = m*X[0]+c
Y[1] = m*X[1]+c

plt.scatter(x,y)
plt.figure(1)
plt.plot(X,Y,'b-')
plt.show()
