#!/usr/bin/env python2
#!-*-coding=utf8 -*-

import time

"""
========================
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""


def ero_sieve(n):
    primes=set(i for i in xrange(3,n+1,2))
    for i in set(primes):
        j=2
        while i*j<n:
            primes.discard(i*j)
            j+=1 
    primes.add(2)
    return primes

def problem10():
    return sum(ero_sieve(2000000))

if __name__=='__main__':
    time1=time.time()
    print problem10()
    time2=time.time()
    print time2-time1	

