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


#FIRST_1000.remove(3)
#FIRST_1000.remove(7)



FIRST_M = ero_sieve(10000)
FIRST_M.remove(2)
FIRST_M.remove(5)
FIRST_M.remove(3)
FIRST_M.remove(7)


"""
(3, 7, 109, 673)
(3, 37, 67, 2377)
(3, 37, 67, 5923)
23, 311, 677
"""
#f2 = [3,7]
"""
f4 = [23, 311, 677]
for i in f4:
    FIRST_1000.remove(i)
"""
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
        if is_prime(int(str(perm[0]) + str(perm[1]))):
            if is_prime(int(str(perm[1]) + str(perm[0]))):
            #prime_sets_of_2.append([perm[0],perm[1]])
                to_add = [perm[0],perm[1]]
                to_add.sort()
                prime_sets_of_2.add(tuple(to_add))

    #print 'made of 2'
    #of_4 = set([])
    #for combo in combinations(prime_sets_of_2, 2):
        #if len(set(combo[0]).symmetric_difference(combo[1])) == 4:
            #of_4.add(combo)

    #print 'made of_4'        
    """
    for prime in FIRST_M:
        primes = list(FIRST_M)
        primes.remove(prime)
        for prime2 in primes:
            if not is_prime(int(str(prime) + str(prime2))):
                break
            if not is_prime(int(str(prime2) + str(prime))):
                break
            else:
                to_add = [prime,prime2]
                to_add.sort()
                print to_add
                prime_sets_of_2.add(tuple(to_add))

    """
    
    """
    Maket prime pair sets of length 3
    """

    print 'made 2', len(prime_sets_of_2)         
    for f2 in prime_sets_of_2:        
        for prime in FIRST_M:
            count = 0
            prime_set = [prime]
            prime_set += list(f2)
            for perm in permutations(prime_set,2):
                if not is_prime(int(str(perm[0]) + str(perm[1]))):
                    break
                else:
                    count += 1
            if count == 6:
                prime_set.sort()
                prime_sets_of_3.add(tuple(prime_set))
    #return prime_sets_of

    
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
                if not is_prime(int(str(perm[0]) + str(perm[1]))):
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
                if not is_prime(int(str(perm[0]) + str(perm[1]))):
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
    print problem60()
    time2=time.time()
    print time2-time1
    


