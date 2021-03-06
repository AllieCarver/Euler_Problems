#!-*-coding=utf8 -*-

import math
import time

"""
========================
Project Euler Problem 37
========================
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove 

digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work 

from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""

def prime(n):
    if n==2:
        return True
    if n==0:
        return False
    for i in xrange(2,int(math.sqrt(n))+1):
        if float(n)%i==0:
            return False
            print n, i
    return True

def problem37():
    the_11=set()
    n=11
    must_start_with='2357'
    must_end_with='37'
    can_only_contain='3791'
#    while n <5000: 
    while len(the_11)<11:
        good=True
        if str(n)[-1] in must_end_with:    
            if str(n)[0] in must_start_with and prime(n):
            
                temp=str(n)[1:-1]
                for i in list(temp):
                    if i not in can_only_contain:
                        good=False
                        break 
            else:
                good=False
        else:
            good=False                  
        
        if good:
            temp_n=list(str(n))
            for i in xrange(len(str(n))-1):
                temp_n.pop(0)
                if not prime(int("".join(temp_n))):
                    good=False 
                    break
        
            temp_n=list(str(n))
            for i in xrange(len(str(n))-1):
                temp_n.pop(-1)
                if not prime(int("".join(temp_n))):
                    good=False
                    break
        else:
            good=False            
        if good:
            the_11.add(n)
        n+=2
          
    return sum(the_11)

if __name__=='__main__':
    time1=time.time()
    print problem37()
    time2=time.time()
    print time2-time1	
