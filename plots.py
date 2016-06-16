# coding: utf-8

import time
from processmanager import Processmanager
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', **{'family': 'serif'})
rc('text', usetex=True)
rc('text.latex', unicode=True)
rc('text.latex', preamble='\\usepackage[utf8]{inputenc}')
rc('text.latex', preamble='\\usepackage[russian]{babel}')


def testall(storagelen, cachelen, number):
    alg = ["lru", "mru", "lfu", "fifo", "slru"]
    print("{0:<6} {1:<6} {2:<6} {3:<6} {4:<12} {5:<12}".format(
          "alg", "hit%", "miss%", "time", "hitcount", "misscount"))
    for _ in range(len(alg)):
        t0 = time.time()
        prmngr = Processmanager(storagelen, alg[_], cachelen)
        cachehit = prmngr.setcountmakestephit(number)
        cachehperc = round(cachehit * 100 / number, 2)
        print("{0:<6} {1:<6.2f} {2:<6.2f} {3:<6.2f} {4:<12} {5:<12}".format(
              alg[_], cachehperc, 100 - cachehperc, time.time() - t0,
              cachehit, number - cachehit))


def plotmissrate(storagelen, cachelenstart, steps, number):
    algs, x = [["lru"], ["mru"], ["lfu"], ["fifo"], ["slru"]], []

    for _ in range(steps):
        x.append(cachelenstart)
        for __ in range(len(algs)):
            prmngr = Processmanager(storagelen, algs[__][0], cachelenstart)
            cachemiss = number - prmngr.setcountmakestephit(number)
            algs[__].append((round(cachemiss * 100 / number, 2)))
        cachelenstart *= 2

    line1, = plt.plot(x, algs[0][1:], 'ro--', label='lru')
    line2, = plt.plot(x, algs[1][1:], 'bs--', label='mru')
    line3, = plt.plot(x, algs[2][1:], 'gv--', label='lfu')
    line4, = plt.plot(x, algs[3][1:], 'cs--', label='fifo')
    line5, = plt.plot(x, algs[4][1:], 'ms--', label='slru')
    plt.axis([0, x[-1] + 0.05 * x[-1], 0, 100])
    plt.xlabel(u"Розмір кешу")
    plt.ylabel(u"Відсоток кеш-промахів")
    plt.legend(title=u"Алгоритм кешування",
               handles=[line1, line2, line3, line4, line5], numpoints=1)
    plt.show()


def plothitrate(storagelen, cachelenstart, steps, number):
    algs, x = [["lru"], ["mru"], ["lfu"], ["fifo"], ["slru"]], []

    for _ in range(steps):
        x.append(cachelenstart)
        for __ in range(len(algs)):
            prmngr = Processmanager(storagelen, algs[__][0], cachelenstart)
            algs[__].append(
                (round(prmngr.setcountmakestephit(number) * 100 / number, 2)))
        cachelenstart *= 2

    line1, = plt.plot(x, algs[0][1:], 'ro--', label='lru')
    line2, = plt.plot(x, algs[1][1:], 'bs--', label='mru')
    line3, = plt.plot(x, algs[2][1:], 'gv--', label='lfu')
    line4, = plt.plot(x, algs[3][1:], 'cs--', label='fifo')
    line5, = plt.plot(x, algs[4][1:], 'ms--', label='slru')
    plt.axis([0, x[-1] + 0.05 * x[-1], 0, 100])
    plt.xlabel(u"Розмір кешу")
    plt.ylabel(u"Відсоток кеш-попадань")
    plt.legend(title=u"Алгоритм кешування",
               handles=[line1, line2, line3, line4, line5], numpoints=1)
    plt.show()


def plothitratetimedepend(storagelen, cachelenstart, steps, number):
    algs = [["lru"], ["lfu"], ["rlQ"], ["rlS"], ["slru"]]
    x = [number // steps * _ for _ in range(steps + 1) if _ != 0]
    for _ in range(len(algs)):
        prmngr = Processmanager(storagelen, algs[_][0], cachelenstart)
        for __ in range(steps):
            n = number // steps
            algs[_].append(round(prmngr.setcountmakestephit(n) * 100 / (n), 2))
    line1, = plt.plot(x, algs[0][1:], 'ro--', label='lru')
    line2, = plt.plot(x, algs[1][1:], 'gv--', label='lfu')
    line3, = plt.plot(x, algs[2][1:], 'bs--', label='rlQ')
    line4, = plt.plot(x, algs[3][1:], 'ks--', label='rlS')
    line5, = plt.plot(x, algs[4][1:], 'ms--', label='slru')
    plt.axis([x[0], x[-1] + 0.05 * x[-1], 35, 70])
    plt.xlabel(u"Кількість кроків")
    plt.ylabel(u"Відсоток кеш-попадань")
    plt.legend(title=u"Алгоритм кешування",
               handles=[line1, line2, line5, line3, line4], numpoints=1)
    plt.show()
