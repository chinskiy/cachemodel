import cachestorage
import numpy as np
import random

class RL:
    def __init__(self, lencache, epsilon=0.08, alpha=0.2, gamma=0.9):
        self.cachestorage = cachestorage.Cachemem(lencache)
        self.start, self.lencache = 0, lencache
        self.epsilon, self.alpha, self.gamma = epsilon, alpha, gamma
        self.actions = np.array([_ for _ in range(lencache)])
        self.stateold, self.actionold = '0', '0'
        self.cachefreq, self.cacheused = [0 for _ in range(lencache)], np.asarray([0 for _ in range(lencache)])
        self.q = {}
        self.reward = 0

    def makestep(self, adress):
        index = self.cachestorage.findindexaddr(adress)
        if self.start < self.lencache:
            if index == -1:
                self.cachestorage.addmemfromds(self.start, adress)
                self.start += 1
                return 0
            else:
                return 1
        else:
            if index == -1:
                state = str(adress)
                if self.stateold != '0':
                    self.learn(self.stateold, self.actionold, self.reward, state)

                action = self.choose_action(state)
                self.cachestorage.addmemfromds(action, adress)

                self.stateold, self.actionold = state, action
                self.reward = -1
                return 0
            else:
                self.reward += 1
                return 1

    def choose_action(self, state):
        if random.random() < self.epsilon:
            action = random.choice(self.actions)
        else:
            q = [self.getQ(state, a) for a in self.actions]
            maxq = max(q)
            if q.count(maxq) > 1:
                best = [i for i in range(len(self.actions)) if q[i] == maxq]
                i = random.choice(best)
            else:
                i = q.index(maxq)
            action = self.actions[i]
        return action

    def getQ(self, state, action):
        return self.q.get((state, action), 0.0)

    def learn(self, state1, action1, reward, state2):
        maxqnew = max([self.getQ(state2, a) for a in self.actions])
        self.learnQ(state1, action1, reward, reward + self.gamma*maxqnew)

    def learnQ(self, state, action, reward, value):
        oldv = self.q.get((state, action), 0)
        if oldv is None:
            self.q[(state, action)] = reward
        else:
            self.q[(state, action)] = oldv + self.alpha * (value - oldv)