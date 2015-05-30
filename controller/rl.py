import cachestorage
import numpy as np
import random

class RL:
    def __init__(self, lencache, epsilon=0.1, alpha=0.2, gamma=0.9):
        self.cachestorage = cachestorage.Cachemem(lencache)
        self.start, self.lencache = 0, lencache
        self.epsilon, self.alpha, self.gamma = epsilon, alpha, gamma
        self.actions, self.stateold, self.statenew, self.actionold = np.array(["lru", "lfu"]), '0', '0', '0'
        self.cachefreq = np.asarray([0 for _ in range(lencache)])
        self.cacheused = np.asarray([0 for _ in range(lencache)])
        self.q = {}
        self.reward, self.hitrate, self.missrate = 0, 0, 0
        self.statistic = [0, 0]

    def makestep(self, adress):
        index = self.cachestorage.findindexaddr(adress)
        if self.start < self.lencache:
            if index == -1:
                self.cachestorage.addmemfromds(self.start, adress)
                self.cacheused += 1
                self.cacheused[self.start] = 0
                self.start += 1
                return 0
            else:
                self.cacheused += 1
                self.cacheused[index] = 0
                self.cachefreq[index] += 1
                return 1
        else:
            if index == -1:
                self.statenew = tuple([self.hitrate, self.missrate])

                if self.stateold != '0':
                    self.learn(self.stateold, self.actionold, self.reward, self.statenew)
                action = self.choose_action(self.statenew)
                if action == "lru":
                    maxind = np.where(self.cacheused == np.max(self.cacheused))[0][0]
                    self.statistic[0] += 1
                else:
                    ind = np.where(self.cachefreq == np.min(self.cachefreq))[0]
                    maxind = np.where(self.cacheused == np.max(self.cacheused[ind]))[0][0]
                    self.statistic[1] += 1
                self.cachestorage.addmemfromds(maxind, adress)

                self.cacheused += 1
                self.cacheused[maxind] = 0
                self.cachefreq[maxind] = 0

                self.stateold, self.actionold = self.statenew, action

                self.hitrate = 0
                self.missrate += 1

                self.reward = -2
                print(self.statistic)
                return 0
            else:
                self.cacheused += 1
                self.cacheused[index] = 0
                self.cachefreq[index] += 1
                self.hitrate += 1
                self.missrate = 0

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