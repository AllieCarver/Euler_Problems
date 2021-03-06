#!-*-coding=utf8 -*-
import math
import time

"""
========================
Project Euler Problem 32
========================
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, 

the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

def pandigital_factors(n):
    pandigital=set(['1','2','3','4','5','6','7','8','9'])
    factors=[]
		
    for i in xrange(1,int(math.sqrt(n))+1):
        if (float(n)/i)%1==0:
			factors.append(i)
    for i in list(factors)[::-1]:
            temp=list(str(i)+str(n/i)+str(n))
            if set(temp)==pandigital and len(temp)==len(pandigital) :
		        return True

def problem32():
    total=set()
    for i in xrange(100000):
        if pandigital_factors(i):
            total.add(i)
    return sum(total)

if __name__=='__main__':
    time1=time.time()
    print problem32()
    time2=time.time()
    print time2-time1	       
