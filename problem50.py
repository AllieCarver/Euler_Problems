#!-*-coding=utf8 -*-

import time


"""
========================
Project Euler Problem 50
========================

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

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

def problem50():
    primes=list(ero_sieve(1000000))
    
    most_consec=int()
    most_consec_sum=int()
    for i in primes[:len(primes)/2]:
        prime_sum=i    
        n=primes.index(i)+1
        count=0
    
        while prime_sum + primes[n] <1000000:
            prime_sum+=primes[n]
            
                
            if count>most_consec:
                if prime_sum in primes:
                    most_consec=count
                    most_consec_sum = prime_sum
                    print most_consec_sum
            n+=1
            count+=1
           
    return most_consec_sum, most_consec


if __name__ == '__main__':        
    time1=time.time()
    print problem50()
    time2=time.time()
    print time2-time1


        
    
    

