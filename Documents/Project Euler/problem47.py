#!-*-coding=utf8 -*-

import math
import time

"""
========================
Project Euler Problem 47
========================
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
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


def prime_factors_count(n):
    done=False
    factors=set([])
    next_prime=3
    while True:
        if n in primeset:    
            return 0
        if n%2==0:
            factors.add(2)
            while n%2==0:
                n/=2
            if n in primeset:
                factors.add(n)
                factors.discard(1)
                return len(factors)
        while not (next_prime in primeset and n % next_prime==0) :
            next_prime+=2		  
                  
        factors.add(next_prime)
        while n %next_prime==0:
            n/=next_prime
                
        if n in primeset:
            factors.add(n)
            factors.discard(1)
            return len(factors)
        next_prime+=2

def problem_47():
    n=210
    while True:
        if prime_factors_count(n+3)==4:
            if prime_factors_count(n+2) == 4:
                if prime_factors_count(n+1)==4:
                    if prime_factors_count(n)==4:
                            return n
                    else:
                        n+=1
                else:
                    n+=2
            else:
                n+=3 
        else:
            n+=4
time1=time.time()
primeset=ero_sieve(150000)
primeset.add(1)
print problem_47()
time2=time.time()
print time2-time1

