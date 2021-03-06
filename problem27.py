#!-*-coding=utf8 -*-

import math
import time

"""
========================
Project Euler Problem 27
========================

Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. 
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 
is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values 
n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum 
number of primes for consecutive values of n, starting with n = 0.
"""
	
def check_prime(n):
	for i in xrange(2, int(math.sqrt(n)+1)):
		if float(n)/i%1==0:
			return False
	else:
		return True


def problem27():
    x=(0,0,0)
    b_list=[i for i in xrange(1,1001,2) if check_prime(i)]
    a_list=[i for i in xrange(-999,1001)]
    for a in a_list:
        for b in b_list:
            n=0
            while n**2 + a*n + b>=0 and check_prime(n**2 + a*n + b) :
                n+=1
            if n>x[0]:
                x=(n,a,b)
    return x, x[1]*x[2]
    
if __name__=='__main__':
    time1=time.time()
    print problem27()
    time2=time.time()
    print time2-time1
