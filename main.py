import math

import numpy as np
import matplotlib.pyplot as plt

perfect = (0,1)

t = open('GT.dsv','r')
truth = np.array(t.read().split('\n')).astype(int)

P = 0
N = 0
for e in truth:
    if e == 0:
        N += 1
    elif e == 1:
        P += 1
def analysis(classificator, m):
    c = open(classificator,'r')
    f = c.read().split('\n')
    results = []
    for line in f:
        results.append(line.split(','))

    results = np.array(results).astype(int)
    TP = np.zeros(len(results[0])).astype(int)
    TN = np.zeros(len(results[0])).astype(int)
    FP = np.zeros(len(results[0])).astype(int)
    FN = np.zeros(len(results[0])).astype(int)

    for alpha in range(0,len(results[0])):
        for line in range(0,len(results)):
            result = results[line][alpha]
            if result == truth[line] and result == 1:
                TP[alpha] += 1
            elif result == truth[line] and result == 0:
                TN[alpha] += 1
            elif result != truth[line] and result == 1:
                FP[alpha] += 1
            elif result != truth[line] and result == 0:
                FN[alpha] += 1

    TPR = TP/P
    FPR = FP/N
    FNR = FN/P
    coords = list(zip(FPR,TPR))
    dists = []
    FPRmin = np.where(FPR == FPR.min())[0]
    secret = np.max(TPR[FPRmin])
    print(classificator)
    print(secret)
    print(np.where(TPR == secret))
    for c in coords:
        x = (perfect[0] - c[0])**2
        y = (perfect[1] - c[1])**2
        dists.append(np.sqrt(x+y))
    a = np.argmin(dists)
    optimum = coords[a]
    '''plt.xlabel('FPR')
    plt.ylabel('TPR')
    plt.plot(FPR,TPR)
    plt.plot([optimum[0]],[optimum[1]],'ro')
    plt.show()'''
    if a < m:
        '''print(a)
        print(classificator)'''
        return a
    else:
        return m

def compare(c,alpha,c6):
    x1 = c_TPR[alpha]
    y1 = c_FPR[alpha]
    c6_TPR = TPR(c6) #list s true positive rates pro každé alfa
    c6_FPR = FPR(c6) #list s false positive rates pro každé alfa

    FPRmin = np.where(c6_FPR == c6_FPR.min())[0]
    i = np.where(c6_TPR == np.max(c6_TPR[FPRmin]))[0]

    x2 = c6_TPR[i]
    y2 = c6_FPR[i]

    dist = lambda x,y: np.sqrt(x**2 + (1-y)**2)

    if dist(x1,y1) > dist(x2,y2):
        return True
    else:
        return False




if __name__ == "__main__":
    m = np.inf
    m = analysis('C1.dsv',m)
    m = analysis('C2.dsv',m)
    m = analysis('C3.dsv',m)
    m = analysis('C4.dsv',m)
    m = analysis('C5.dsv',m)

