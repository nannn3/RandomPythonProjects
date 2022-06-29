# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 08:12:00 2022

@author: Tristen
"""
import time
import string
import random
import matplotlib.pyplot as plt


def timer(func):
    def wrap(s1,s2):
        start=time.time()
        func(s1,s2)
        end=time.time()
        return end-start
    return wrap
        
@timer        
def is_anagram1(s1,s2):
    if len(s1) != len(s2):
        return False
    else:
        for i in range(len(s1)):
            found=False
            for j in range(len(s1)):
                if s1[i]==s2[j]:
                    found=True
                    break
            if not found:
                return False
        return True

@timer
def is_anagram2(s1,s2):
    if len(s1)!=len(s2):
        return False
    s1=sorted(list(s1))
    s2=sorted(list(s2))
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            return False
    return True
@timer
def is_anagram3(s1,s2):
    c1=[0]*26
    c2=[0]*26
    for i in range(len(s1)):
        pos=ord(s1[i])-ord('a')
        c1[pos]=c1[pos]+1
    for i in range(len(s2)):
        pos=ord(s2[i])-ord('a')
        c2[pos]=c2[pos]+1
    for j in range(len(c1)):
        if c1[j] != c2[j]:
            return False
    return True
    
    
    
if __name__ == '__main__':
    time1=[]
    time2=[]
    time3=[]
    size=[]
    for i in range(8):
        s1=[0]*(10**i)
        s2=[0]*(10**i)
        for i in range(len(s1)):
            s1[i]=random.choice(string.ascii_letters)
            s1[i]=s1[i].lower()
            s2[i]=s1[i]
        random.shuffle(s1)
        size.append(len(s1))
        time1.append(is_anagram1(s1,s2))
        time2.append(is_anagram2(s1,s2))
        time3.append(is_anagram3(s1,s2))
        
    plt.plot(size,time1,label="is_anagram1")
    plt.plot(size,time2,label="is_anagram2")
    plt.plot(size,time3,label="is_anagram3")
    plt.ylabel("Time(s)")
    plt.xlabel("Number of letters in each anagram")
    plt.xscale('log')
    plt.legend()
    plt.show()