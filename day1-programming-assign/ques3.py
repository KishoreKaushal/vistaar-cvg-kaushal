#!/usr/bin/python3

import numpy as np

Shape = input().split(',')
a = int(Shape[0])
b = int(Shape[1])

def f(i,j):
    return i*j

result = np.fromfunction(f, (a,b) , dtype=int)
print(result)
