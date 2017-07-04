#!/usr/bin/python3

def newtonraphson(f, fPrime , x0=1, TOL = 1e-5, EPSILON = 1e-14 , maxIter = 20):

    foundSolution = False

    for i in range(1,maxIter+1):
        y = f(x0)
        yPrime = fPrime(x0)
        if(abs(yPrime) < EPSILON ):
            break

        x1 = x0 - y/yPrime

        if(abs(x1-x0) <= TOL*abs(x1)):
            foundSolution = True
            break

        x0 = x1

    if(foundSolution):
        return x1
    else:
        return "Method Failed"
