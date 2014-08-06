#!-*-coding=utf8 -*-
from itertools import permutations as perm
import time

"""
========================
Project Euler Problem 49
========================

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,

is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit

numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this

property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

def ero_sieve(rangelimit):
    primes=set(i for i in xrange(3,rangelimit+1,2))
    for i in set(primes):
        j=2
        while i*j<rangelimit:
            primes.discard(i*j)
            j+=1 
    primes.add(2)
    return primes

def problem49():
    primes=ero_sieve(9999)
    for i in set(primes):
        if i<1001:
            primes.discard(i)
    for i in set(primes):
        permutations=set(int(''.join(j)) for j in perm(str(i)) if int(''.join(j)) in primes)
        if len(permutations)>=3:
            permutations=list(permutations)
            permutations.sort()
            for k in xrange(len(permutations)-2):
                if permutations[k+2]-permutations[k+1]==permutations[k+1]-permutations[k]:
                    return str(permutations[k])+str(permutations[k+1])+str(permutations[k+2])
   
if __name__=='__main__':                    
    time1=time.time()
    print problem49()
    time2=time.time()
    print time2-time1
        
            

