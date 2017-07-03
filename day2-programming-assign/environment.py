
import numpy as np
#from epsilonGreedy import epsilonGreedy
import matplotlib.pyplot as plt

#########################################################


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
        self.Q[index] += (reward - self.Q[index])/self.count[index]


########################################################

def sampler():
	return np.random.normal()

def interaction(n,true_rew):
	return true_rew[n]+sampler()

def generate_true_rew():
	true_rew=[]
	for i in range(10):
		true_rew.append(sampler())
	return true_rew

def main(epsilon,true_rew,iterations):
	n=10
	interact=epsilonGreedy(epsilon,n)
	average_rew=[]
	for i in range(iterations):
		n=interact.pullArms()
		reward=interaction(n,true_rew)
		interact.updateVal(n,reward)
		#print(str(i+1)+'\t'+str(n+1)+'\t'+str(np.argmax(interact.expected_reward)+1))
		average_rew.append(interact.Q[n])
	return average_rew

print("ok")

iterations=1000
bandits=2000
average_reward0=np.zeros(iterations)
average_reward0_01=np.zeros(iterations)
average_reward0_1=np.zeros(iterations)
for i in range(bandits):
	print(i)
	true_rew=generate_true_rew()
	average_reward0=np.add(average_reward0,main(0,true_rew,iterations))
	average_reward0_01=np.add(average_reward0_01,main(0.01,true_rew,iterations))
	average_reward0_1=np.add(average_reward0_1,main(0.1,true_rew,iterations))
eps0,=plt.plot(average_reward0/float(bandits),label='e=0')
eps0_01,=plt.plot(average_reward0_01/float(bandits),label='e=0.01')
eps0_1,=plt.plot(average_reward0_1/float(bandits),label='e=0.1')
plt.show()
