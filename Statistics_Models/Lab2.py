# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: Tristen Miller (trkmille@ucsc.edu)

@discription: Lab2 for statistics, demonstartes the question:
    An urn contains 𝑎 azure balls and 𝑐 carmine balls, where 𝑎 > 0 and 𝑐 > 0. Balls
are selected from the urn at random and discarded, until the first time a selected ball
has a color different from its predecessor. That ball is then replaced, and the
procedure is restarted. The process continues until the last ball is discarded. Show
that this last ball is equally likely to be azure or carmine.

For a=[10,50,90] and the total number of balls is 100
"""
from random import choice, shuffle
from datetime import datetime


class balls():
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return f"Ball({self.color})"

    def __eq__(self, o):
        return self.color == o.color


def main(a):
    a_count = 0
    for _ in range(2000):
        total = 100
        jar = []
        last_pick = None
        for i in range(a):
            jar.append(balls("Azure"))
        for i in range(total-a):
            jar.append(balls("Carmine"))
        shuffle(jar) #not strictly required, but no real reason not to

        while total != 0:
            pick = choice(jar)
            if last_pick is None or pick == last_pick:
                jar.remove(pick)
                total -= 1
                last_pick = pick
            else:
                pick = None
                last_pick = None

        if pick.color == "Azure":
            a_count += 1
    with open("Report2.doc", 'a') as file:
        file.write(
            f"\nThe last ball was Azure in {a_count} out of 2000 trials when there are {a} Azure balls, for a realtive frequence of {a_count/2000}\n")


if __name__ == "__main__":
    with open("Report2.doc",'w') as file:
        file.write(f"report autogenerated {str(datetime.now())}\n Tristen Miller\n")
    sizes = [10, 50, 90]
    for size in sizes:
        main(size)
    with open("Report2.doc",'a') as file:
        file.write(f"\n End autogeneration =================================== {str(datetime.now())}\n")
