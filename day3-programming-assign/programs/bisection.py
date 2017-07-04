#!/usr/bin/python3

def bisection(f,a,b, TOL = 1e-5, maxIter = 100):
    if (f(a)*f(b))>0:
        return " Method Failed: f(a)*f(b) is not less than zero."
    else:
        i = 0
        while i < maxIter:
            c = float((a+b))/2
            if f(c)==0 or (b-a)/2 < TOL:
                return c
            i+=1
            if f(c)*f(a)>0:
                a = c
            else:
                b = c

        return "Method Failed"
