import time
import processmanager
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', **{'family': 'serif'})
rc('text', usetex=True)
rc('text.latex', unicode=True)
rc('text.latex', preamble='\\usepackage[utf8]{inputenc}')
rc('text.latex', preamble='\\usepackage[russian]{babel}')


def testall(datastoragelen, cachelen, number):
    alg = ["lru", "mru", "lfu", "fifo"]

    print("alg".ljust(5), "hit%".ljust(6), "miss%".ljust(6), "time".ljust(6),
          "hitcount".ljust(12), "misscount".ljust(12))
    for _ in range(len(alg)):
        t0 = time.time()
        prmngr = processmanager.Processmanager(datastoragelen, alg[_], cachelen)
        cachehit = prmngr.setcountmakestephit(number)
        cachehperc = round(cachehit * 100/number, 2)
        print(alg[_].ljust(5), str(cachehperc).ljust(6), str(round(100 - cachehperc, 2)).ljust(6),
              str(round(time.time() - t0, 2)).ljust(6), str(cachehit).ljust(12),
              str(number - cachehit).ljust(12))


def plotmissrate(datastoragelen, cachelenstart, steps, number):
    algs, x = [["lru"], ["mru"], ["lfu"], ["fifo"]], []

    for _ in range(steps):
        x.append(cachelenstart)
        for __ in range(len(algs)):
            prmngr = processmanager.Processmanager(datastoragelen, algs[__][0], cachelenstart)
            cachemiss = number - prmngr.setcountmakestephit(number)
            algs[__].append((round(cachemiss * 100 / number, 2)))
        cachelenstart *= 2

    line1, = plt.plot(x, algs[0][1:], 'ro--', label='lru')
    line2, = plt.plot(x, algs[1][1:], 'bs--', label='mru')
    line3, = plt.plot(x, algs[2][1:], 'gv--', label='lfu')
    line4, = plt.plot(x, algs[3][1:], 'cs--', label='fifo')
    plt.axis([0, x[-1] + 0.05 * x[-1], 0, 100])
    plt.xlabel("Розмір кешу")
    plt.ylabel("Відсоток кеш-промахів")
    plt.legend(title="Алгоритм кешування", handles=[line1, line2, line3, line4], numpoints=1)
    plt.show()


def plothitrate(datastoragelen, cachelenstart, steps, number):
    algs, x = [["lru"], ["mru"], ["lfu"], ["fifo"]], []

    for _ in range(steps):
        x.append(cachelenstart)
        for __ in range(len(algs)):
            prmngr = processmanager.Processmanager(datastoragelen, algs[__][0], cachelenstart)
            algs[__].append((round(prmngr.setcountmakestephit(number) * 100 / number, 2)))
        cachelenstart *= 2

    line1, = plt.plot(x, algs[0][1:], 'ro--', label='lru')
    line2, = plt.plot(x, algs[1][1:], 'bs--', label='mru')
    line3, = plt.plot(x, algs[2][1:], 'gv--', label='lfu')
    line4, = plt.plot(x, algs[3][1:], 'cs--', label='fifo')
    plt.axis([0, x[-1] + 0.05 * x[-1], 0, 100])
    plt.xlabel("Розмір кешу")
    plt.ylabel("Відсоток кеш-попадань")
    plt.legend(title="Алгоритм кешування", handles=[line1, line2, line3, line4], numpoints=1)
    plt.show()


def plothitratetimedepend(datastoragelen, cachelenstart, steps, number):
    algs, x = [["lru"], ["mru"], ["lfu"], ["fifo"]], [number // steps * _ for _ in range(steps + 1) if _ != 0]
    print(x)
    for _ in range(len(algs)):
        prmngr = processmanager.Processmanager(datastoragelen, algs[_][0], cachelenstart)
        for __ in range(steps):
            algs[_].append((round(prmngr.setcountmakestephit(number // steps) * 100 / (number // steps), 2)))

    print(algs)
    line1, = plt.plot(x, algs[0][1:], 'ro--', label='lru')
    line2, = plt.plot(x, algs[1][1:], 'bs--', label='mru')
    line3, = plt.plot(x, algs[2][1:], 'gv--', label='lfu')
    line4, = plt.plot(x, algs[3][1:], 'cs--', label='fifo')
    plt.axis([x[0], x[-1] + 0.05 * x[-1], 0, 100])
    plt.xlabel("Кількість кроків")
    plt.ylabel("Відсоток кеш-попадань")
    plt.legend(title="Алгоритм кешування", handles=[line1, line2, line3, line4], numpoints=1)
    plt.show()