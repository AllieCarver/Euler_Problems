#!-*-coding=utf8 -*-

import math
import time

"""
========================
Project Euler Problem 21
========================

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""
	
def factors(n):
	factors=[]
	for i in xrange(1,int(math.sqrt(n))+1):
		if (float(n)/i)%1==0:
			factors.append(i)	
	for i in list(factors)[::-1]:
		if n/i < n:
		    factors.append(n/i)
	return factors


def problem21():
    amicable=set([])
    for i in range(10001):
        if i==sum(factors(sum(factors(i)))) and i!=sum(factors(i)):
            amicable.add(i)
            amicable.add(sum(factors(i)))
    return sum(amicable)            

if __name__=='__main__':
    time1=time.time()
    print problem21()
    time2=time.time()
    print time2-time1
