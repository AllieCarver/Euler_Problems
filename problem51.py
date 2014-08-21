#!-*-coding=utf8 -*-

import time


"""
========================
Project Euler Problem 51
========================

By replacing the 1st digit of the 2-digit number *3, it turns out that siprime_candidates 

of the nine possiblevalues: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit 

number is the first eprime_candidatesample having seven primes among the ten generated numbers, 

yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 

Consequently 56003, being the first member of this family, is the smallest prime 

with this property.

Find the smallest prime which, by replacing part of the number (not necessarily 

adjacent digits) with the same digit, is part of an eight prime value family.
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

def problem51():
        
    prime_candidates= [str(i) for i in ero_sieve(1000000) if len(set(str(i)[:-1])) <= len(list(str(i)[:-1]))-2 and str(i)[-1]=='3'and i > 100000]
    for i in list(prime_candidates):
        repeat=False
        for j in xrange(10):
            if i[:-1].count(str(j)) >=3:
                repeat=True
        if not repeat:
            prime_candidates.remove(i)       

    for i in prime_candidates:
        family=[i]
        repeat=str()
        for char in i[:-1]:
            if i.count(char)>=3:
                repeat=char
                break
        for k in xrange(int(repeat)+1,10):
            test=i.replace(repeat, str(k))
            if test in prime_candidates:
                family.append(test)                
        if len(family)>=8:
            return family[0]
   
if __name__=='__main__':
    time1=time.time()
    print problem51()
    time2=time.time()
    print time2-time1
        
            
                
    
