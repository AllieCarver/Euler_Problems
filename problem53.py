#!-*-coding=utf8 -*-

import time
from math import factorial as fact

"""
========================
Project Euler Problem 53
========================

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general, nCr = n!/r!(n−r)!, where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
"""

def problem53():
    count=0
    for n in xrange(1,101):
        for r in xrange(1,n+1):
            if fact(n)/(fact(r)*fact(n-r)) > 1000000:
                count+=1
         
    return count

if __name__=='__main__':
    time1=time.time()
    print problem53()
    time2=time.time()
    print time2-time1
