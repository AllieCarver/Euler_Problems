#!-*-coding=utf8 -*-

import math
import time

"""
========================
Project Euler Problem 23
========================

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, 

the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the 

sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 

can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis 

even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

"""

def abundant(n):
    factors=set([])
    for i in xrange(1,int(math.sqrt(n))+1):
		if n%i==0:
			factors.add(i)
    for i in set(factors):
            if n/i != n:
		        factors.add(n/i)   
    return sum(factors)>n

def problem23():
    abundant_nums=set([i for i in xrange(12,28123) if abundant(i)])
    not_abundant_sums=set(xrange(1,28123))
    abundant_sums=set([])
    for i in abundant_nums:
        for j in abundant_nums:
            if (i+j) < 28123:
                abundant_sums.add(i+j)
    return sum(not_abundant_sums.difference(abundant_sums))


if __name__=='__main__':
    time1=time.time()
    print problem23()
    time2=time.time()
    print time2-time1	

