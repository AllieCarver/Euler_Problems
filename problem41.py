#!-*-coding=utf8 -*-

import math
import time

"""
========================
Project Euler Problem 41
========================
We shall say that an n-digit number is pandigital if it makes 

use of all the digits 1 to n exactly once. 

For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from itertools import permutations as perm

def prime(n):
    if n==2:
        return True
    if n==0:
        return False
    for i in xrange(2,int(math.sqrt(n))+1):
        if float(n)%i==0:
            return False
            print n, i
    return True

def problem41():
    front="765"
    ends_with='13'
    largest=int()
    for i in xrange(1233,4322,2):
        temp=front+str(i)
        if temp[-1] in ends_with:
            if "0" not in temp:
                if "9" not in temp:
                    if "8" not in temp:          
                        if len(set(temp))==7:
                            if prime(int(temp)):
                                if int(temp)>largest:
                                    largest=int(temp)
    return largest
time1=time.time()
print problem41()
time2=time.time()
print time2-time1

def pandigital(n):
    c=str(n)
    if "0" not in c:
        if "8" not in c:
            if "9" not in c:
                if len(set(c))==7:
                    return True
    
    return False
            
def problem41b():
    n=7654321
    while not (pandigital(n) and prime(n)):
        n-=2
    return n

if __name__=='__main__':
    time1=time.time()
    print problem41b()
    time2=time.time()
    print time2-time1	                                   
