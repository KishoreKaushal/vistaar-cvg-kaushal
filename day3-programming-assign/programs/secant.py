#!/usr/bin/python3


def secant(f , xx , maxIter=20):
    calc = 0.0
    X = [float(xx[0]), float(xx[1])]
    for i in range(2,maxIter+3):
         calc = float(X[i-1] - f(X[i-1]) * ( (X[i-1] - X[i-2])  / (f(X[i-1]) - f(X[i-2])) ))
         X.append(calc)

    return float(X[maxIter+2])
