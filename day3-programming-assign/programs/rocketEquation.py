#!/usr/bin/python3

from sys import argv , exit
from math import *
from secant import *
from bisection import *
from newtonraphson import *

if len(argv)!=2:
    print("Usage: ", str(argv[0]) , "mode-number")
    print("1 : Bisection\n2 : Newton-Raphson\n3 : Secant")
    exit(1)

def fPrime(t, v=335.0, u = 2510.0, M0=2.8*1e6 , m = 13.3*1e3, g=9.81):
    return float((u*m)/(M0 - m*t) -g)

def func(t, v=335.0, u = 2510.0, M0=2.8*1e6 , m = 13.3*1e3, g=9.81):
    return float(u*log((M0)/(M0 - m*t)) - g*t - v)

mode = int(argv[1])

if(mode == 1):
    print("Using Bisection Method: ")
    print(bisection(func, 0, 200))
elif(mode == 2):
    print("Using Newton-Raphson Method: ")
    print(newtonraphson(func, fPrime, 60))
elif(mode == 3):
    print("Using Secant Method: ")
    print(secant(func, [0, 200], 10))
else:
    print("Undefined Mode NUmber")
