#!/usr/bin/env python2
#!-*-coding=utf8 -*-
from math import sqrt as sqrt
import time


"""
========================
Project Euler Problem 07
========================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""
#Fastest way to creat primes	
def ero_sieve(n):
    primes=set(i for i in xrange(3,n+1,2))
    for i in set(primes):
        j=2
        while i*j<n:
            primes.discard(i*j)
            j+=1 
    primes.add(2)
    return primes

def problem07():
    primes=list(ero_sieve(200000))
    primes.sort()
    return primes[10000]
	
	
if __name__=='__main__':
    time1=time.time()
    print problem07()
    time2=time.time()
    print time2-time1
