#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

class epsilonGreedy:

    def __init__(self, eps=0.01 , N=10):
        self.epsilon = eps
        self.N = N
        self.Q = np.random.random(self.N)*0.0001
        self.count = np.zeros(self.N)

    def pullArms(self):
        rand = np.random.random()
        if rand<self.epsilon:
            return np.random.randint(self.N)
        else:
            return np.argmax(self.Q)

    def updateVal(self, index , reward):
        self.count[index]+=1
        self.Q[index] += (reward - self.Q[i])/self.count[i]
