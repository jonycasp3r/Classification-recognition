import argparse
import os
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

def bayes(train, test, output):
    classes = {}
    names = []
    clss = []
    cl_set = set()

    f = open(train+"/truth.dsv",'r')
    truth = f.read()
    for line in truth.splitlines():
        name,cls = line.split(':')
        names.append(name)
        clss.append(cls)
        cl_set.add(cls)
        classes[cls] = classes.get(cls, 0) + 1
    img = np.ravel(plt.imread(train+'/'+name)).astype(int)


    posts = np.zeros(shape=(len(classes.keys()),len(img),256)).astype(float)

    cl = list(cl_set)
    cl.sort()
    priors = np.zeros(len(cl))

    for i,c in enumerate(cl):
        priors[i] = classes[c]/len(clss)


    for i,name in enumerate(names):
        img = plt.imread(train+'/'+name)
        flat = (np.ravel(img)*255)
        flat = flat.astype(int)
        for j,intensity in enumerate(flat):
            posts[cl.index(clss[i])][j][intensity] += 1

    np.set_printoptions(threshold=np.inf)

    for c in range(0,len(cl_set)):
        for p in range(0,len(img)):
            posts[c][p] /= classes[cl[c]]

    to_test = os.listdir(test)
    out = ""
    for f in to_test:
        img = plt.imread(test+'/'+f)
        flat = (np.ravel(img)*255).astype(int)
        dec = []
        for i,c in enumerate(cl):
            prob = priors[i]
            for j,intensity in enumerate(flat):
                prob *= posts[i][j][intensity]
            dec.append(prob)
        out += f+":"+cl[np.argmax(dec)]+"\n"
    f = open(output,'w')
    f.write(out)
    f.close()



    #classes:width*height,intensities


def knn(train,test,output,k):
    if k == 0:
        k = 3

    data = []
    names = []
    labels = []
    f = open(train + "/truth.dsv", 'r')
    truth = f.read()
    for line in truth.splitlines():
        name, cls = line.split(':')
        names.append(name)
        labels.append(cls)

    for name in names:
        img = plt.imread(train+'/'+name)
        flat = (np.ravel(img) * 255).astype(int)
        data.append(flat)
    data = np.array(data)
    to_test = os.listdir(test)
    out = ""
    for f in to_test:
        img = plt.imread(test+'/'+f)
        flat = (np.ravel(img)*255).astype(int)
        dec = []
        dists = np.sum(np.subtract(data,flat)**2,axis=1)
        lab = np.argsort(dists)[:k]
        for l in lab:
            dec.append(labels[l])
        c = Counter(dec).most_common(1)[0][0]
        out += f + ":" + c + "\n"

    if output != None:
        f = open(output,'w')
        f.write(out)
        f.close()



if __name__=='__main__':
    p = argparse.ArgumentParser(description='Learn and Classify image data')

    p.add_argument("-k", type=int,action='store', help="run K-NN classifier, if K is 0 the code may decide about proper K by itself")
    p.add_argument("-b", action='store_true',help="run Naive Bayes classifier")
    p.add_argument('-o', required=False,type=str, action='store',help='run Naive Bayes classifier')

    p.add_argument('train_path', type=str, help='Path to the training data')
    p.add_argument('test_path', type=str,help='Path to the testing data')

    args = p.parse_args()

    train = args.train_path
    test = args.test_path

    b = args.b
    k = args.k
    o = args.o

    if b == True:
        bayes(train,test,o)

    if k != None:
        knn(train,test,o,k)