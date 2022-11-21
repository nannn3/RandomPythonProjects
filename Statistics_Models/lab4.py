"""
@author Tristen Miller (trkmille@ucsc.edu)
@discription A model for lab4 answering the prompt:Suppose you have two coins for which
𝑃(Coin 1 = heads) = 𝑝,
and
𝑃(Coin 2 = heads) = 𝑞,
Flip Coin 1 until the first head appears, counting the number of flips. Let 𝑁 be the number of flips in
this first sequence. Next, perform 𝑁 flips of Coin 2, counting the number of heads. Let 𝑌 be the number
of heads in this second sequence. Note that 𝑁 is Geometric with parameter 𝑝. If 𝑋𝑖 is the random
variable
𝑋𝑖 = { 1 if the 𝑖th flip of Coin 2 is heads
0 if the 𝑖th flip of Coin 2 is tails
then we see each 𝑋𝑖 is Bernoulli with parameter 𝑞. We assume of course that all coin flips are
independent, so the set {𝑁, 𝑋1, 𝑋2, ... } is independent. Observe that
𝑌 = 𝑋1 + 𝑋2 + ⋯ ⋯ ⋯ + 𝑋𝑁
is the sum of a random number of independent identically distributed (iid) random variables. We will
derive the mean and variance of 𝑌, in terms of 𝑝 and 𝑞, in lecture. Your goal in this assignment will be
to compute both 𝐸[𝑌] and 𝑉𝑎𝑟(𝑌) experimentally, for various values of 𝑝 and 𝑞. Each approximate
mean and variance you compute in this project will be obtained by performing 10,000 trials of the above
experiment.
:"""
from random import random
import numpy as np

def coinFlip(p):
    '''


    Parameters
    ----------
    p : float
        percent chance of landing on Heads.

    Returns
    -------
    str
        Either H for heads or T for tails.

    '''
    if random() < p:
        return "H"
    else:
        return "T"


def getAverage(ls: list):
    '''
    Parameters
    ----------
    ls : list
        list of numbers to find the average for.

    Returns
    -------
    tot : float
        the average of the list

    '''
    if len(ls) == 0:
        return 0
    tot = 0
    for i in ls:
        tot += i
    tot /= len(ls)
    return tot


def testAverage():
    'Quick check that I did not mess up getAverage()'
    assert(getAverage([1 for i in range(10)]) == 1)
    ls = [-1, 1]
    assert(getAverage(ls) == 0)
    assert(getAverage([]) == 0)


def getVariance(ls: list):
    '''
    Parameters
    ----------
    ls : list
        list to get a variance and mean from.

    Returns
    -------
    tot,mean:(float,float)
        the variance and the mean of the list of numbers

    '''
    if len(ls) == 0:
        return 0, 0
    mean = getAverage(ls)
    tot = 0
    for i in ls:
        X = (i-mean)**2
        tot += X
    tot /= (len(ls)-1)
    return tot, mean  # We're going to need the mean anyway, no need to make a seperate call


def testVariance():
    'quick check that I did variance right'
    ls = [1 for i in range(10)]
    assert(getVariance(ls)[0] == 0)
    ls = [1, 2, 3, 4]
    assert(getVariance(ls)[0] == 5/3)
    assert(getVariance([])[0] == 0)


def single_trial(p, q):
    x = 0
    Y = []
    while(True):
        if coinFlip(p) == "H":
            break
        x += 1
    for _ in range(x):
        if coinFlip(q) == "H":
            Y.append(1)
        else:
            Y.append(0)
    var, mean = getVariance(Y)
    return var, mean


def main():
    probs = [.1*i for i in range(1, 10)]
    size=len(probs) #we don't need a zero row/column
    means=np.zeros((size,size))
    varsMat=np.zeros((size,size))
    for p in probs:
        indexP=int((p*10)-1)
        for q in probs:
            indexQ=int((q*10)-1)
            for _ in range(10000):
                var, mean = single_trial(p, q)
                means[indexP][indexQ] +=mean
                varsMat[indexP][indexQ]+= var
    print(means)


if __name__ == '__main__':
    testAverage()
    testVariance()
    main()
