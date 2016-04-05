# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 00:50:27 2015

@author: killerdigby
"""

import time
from itertools import combinations, permutations
from eulertools import ero_sieve

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
"""
PRIMESM = ero_sieve(10000000)
PRIMESK = ero_sieve(1000000)
PRIMES = ero_sieve(100000)

print 'made primes lists'


FIRST_M = ero_sieve(10000)
FIRST_M.remove(2)
FIRST_M.remove(5)
FIRST_M.remove(3)
FIRST_M.remove(7)

PRIMESM.difference_update(PRIMESK)
PRIMESK.difference_update(PRIMES)
PRIMES.difference_update(FIRST_M)
"""
def l8(num):
    return is_prime(num)
    
def l7(num):
    return num in PRIMESM

def l6(num):
    return num in PRIMESK
    
def l5(num):
    return num in PRIMES
      
def l4(num):
    return num in FIRST_M


use_fun = {2:l4, 3:l4, 4:l4, 5: l5, 6:l6, 7:l7, 8:l8}


def problem60():
    test_set = []
    prime_sets = []
    prime_sets_of_2 = set([])#[[a[0],[1]] for a in combinations(FIRST_1000,2)]
    prime_sets_of_3 = set([])
    prime_sets_of_5 = []

    """
    Make prime pair sets of length 2
    """
    for perm in combinations(FIRST_M, 2):
        num = int(str(perm[0]) + str(perm[1]))
       
        if  use_fun[len(str(num))](num):
            if use_fun[len(str(num))](int(str(perm[1]) + str(perm[0]))):
                to_add = [perm[0],perm[1]]
                to_add.sort()
                prime_sets_of_2.add(tuple(to_add))
                    
    
    """
    Maket prime pair sets of length 3
    """
                    
    print 'made 2', len(prime_sets_of_2)         
    for f2 in prime_sets_of_2:        
        for prime in FIRST_M:
            count = 0
            prime_set = [prime]
            prime_set += list(f2)
            for perm in combinations(prime_set,2):
                num = int(str(perm[0]) + str(perm[1]))
                if not use_fun[len(str(num))](num):
                    break
                elif not use_fun[len(str(num))](int(str(perm[1]) + str(perm[0]))):
                    break
                else:
                    count += 1            
     
 
            if count == 3:
                prime_set.sort()
                prime_sets_of_3.add(tuple(prime_set))

    
    """
    make prime pair sets of length 4 
    """
    print 'made 3', len(prime_sets_of_3)
    for f4 in prime_sets_of_3:        
        for prime in FIRST_M:
            count = 0
            prime_set = [prime]
            prime_set += list(f4)
            for perm in permutations(prime_set,2):
                num = int(str(perm[0]) + str(perm[1]))
                #if not is_prime(int(str(perm[0]) + str(perm[1]))):
                 #   break
                if not use_fun[len(str(num))](num):
                    break
                
                else:
                    count += 1
            if count == 12:
                prime_sets.append(prime_set)
                #test_set.append((sum(prime_set), prime_set))
        
    #return str(min(test_set)) +"\n"+ str(test_set)



    """
    Make prime pair sets of 5
    """

    print 'made 4', len(prime_sets)
    for set_of_4 in prime_sets:
        for prime in FIRST_M:
            count = 0
            prime_set = [prime]
            prime_set += list(set_of_4)
            for perm in permutations(prime_set,2):
                num = int(str(perm[0]) + str(perm[1]))
                #if not is_prime(int(str(perm[0]) + str(perm[1]))):
                 #   break
                if not use_fun[len(str(num))](num):
                    break
                else:
                    count += 1
            if count == 20:
                #return sum(prime_set),prime_set
                #print sum(prime_set), prime_set
                prime_sets_of_5.append((sum(prime_set),prime_set))        
    return  str(min(prime_sets_of_5)) +"\n"+ str(prime_sets_of_5)
    
if __name__=='__main__':
    time1=time.time()
    #print problem60()
    time2=time.time()
    print time2-time1
    


import itertools as iter 
primes = ero_sieve(10000)
set_size = 5

def make_chain(chain):
    if len(chain) == set_size:
        return chain 
    for p in primes:
        if p > chain[-1] and all_prime(chain+[p]):
            new_chain = make_chain(chain+[p])
            if new_chain:
                return new_chain
    return False  
        
def all_prime(chain):
    return all(is_prime(int(str(p[0]) + str(p[1]))) for p in iter.permutations(chain, 2))

chain = 0
while not chain:
    chain = make_chain([primes.pop()])

print "Project Euler 60 Solution =", sum(map(int, chain)), chain
