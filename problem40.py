#!-*-coding=utf8 -*-

import time

"""
========================
Project Euler Problem 40
========================

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""

def problem40():
    fraction=str()
    n=1
    value=1
    while len(fraction)<1000000:
        fraction+=str(n)
        n+=1
    for i in xrange(7):
        value*=int(fraction[(10**i)-1])
    return value, n

if __name__=='__main__':
    time1=time.time()
    print problem40()
    time2=time.time()
    print time2-time1	

