#!-*-coding=utf8 -*-

import time
from math import sqrt as sqrt

"""
========================
Project Euler Problem 58
========================

Starting with 1 and spiralling anticlockwise in the following way, a 
square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom 
right diagonal, but what is more interesting is that 8 out of the 13 
numbers lying along both diagonals are prime; that is, a ratio of 
8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a 
square spiral with side length 9 will be formed. If this process 
is continued, what is the side length of the square spiral for which 
the ratio of primes along both diagonals first falls below 10%?
"""
def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes:
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])
 
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]

def check_prime(n):
    if n==2:
        return True
    if n%2==0:
        return False
    for i in xrange(3, int(sqrt(n)+1),2):
        if float(n)%i==0:
            return False	
    else:
        return True    

def problem58():
    numbers=[1]   
    total=1
    prime_count=0
    i=3
    while True:
        numbers.extend([i**2, (i**2-(i-1)), (i**2-2*(i-1)), (i**2-3*(i-1))])
        for num in numbers[-4:]:
            if is_prime(num):
                prime_count+=1
        total+=4
        if float(prime_count)/total < 0.10:
            return i
        i+=2

if __name__=='__main__':
    time1=time.time()
    print problem58()
    time2=time.time()
    print time2-time1
