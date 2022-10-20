# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 06:45:17 2022

@author: Tristen Miller (trkmille@ucsc.edu)

@discription: Models the Question:
    Alice and Bob have 2𝑛 + 1 coins, each with probability of a head equal to 1/2.
Bob tosses 𝑛 + 1 coins, while Alice tosses the remaining n coins. Show that the
probability that after all the coins have been tossed, Bob will have gotten more
heads than Alice is 1/2.
Now suppose that we do the same sequence of experiments for 𝑛 ∈ {5, 10, 50, 100}, with 2𝑛 + 1 loaded
coins. Suppose the probability of heads is equal to 𝑝, for 𝑝 ∈ {0.2, 0.3, 0.4, 0.6, 0.7, 0.8}. 

"""
from random import random
from datetime import datetime


def coin_flip(p=.5):
    '''
    Parameters
    ----------
    p : float
        probability of landing on heads. The default is .5.

    Returns
    -------
    rtype: str
    returns either 'H' or 'T'.

    '''
    return 'H' if random() < p else 'T'
# End coin_flip


def main(p=.5):
    ns = [5, 10, 50, 100]
    for n in ns:
        Bob_more = 0
        for _ in range(1000):
            # reset the count at the start of each new trial
            Bob_heads = 0
            Alice_heads = 0
            for _ in range(n):
                if coin_flip(p) == 'H':
                    # Flip Bob's coin and record Heads
                    Bob_heads += 1
                if coin_flip(p) == 'H':
                    # Flip Alice's coin and record Heads
                    Alice_heads += 1
            # End for
            if coin_flip(p) == 'H':
                # Bob flips one more coin than Alice
                Bob_heads += 1
            if Bob_heads > Alice_heads:
                Bob_more += 1
        # End for
        with open('Report.doc', 'a') as file:
            file.write("\nBob got more heads in "+str(Bob_more) + " trials when n = "+str(n) + " and p = "+str(p) +
                       "\nThe realitive frequency of Bob having more heads is " + str(Bob_more/1000)+"\n")
    # End for

# End Main


if __name__ == '__main__':
    with open('Report.doc', 'w') as file:
        file.write(str(datetime.now())+"\nReport auto-generated\nTristen Miller\n")
    main()
    probs = [.2, .3, .4, .6, .7, .8]
    for prob in probs:
        main(prob)
    # End for
    with open('Report.doc', 'a') as file:
        file.write("===============End auto-generation================"+str(datetime.now()))
