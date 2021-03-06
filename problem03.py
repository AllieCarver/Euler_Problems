#!/usr/bin/env python2
#!-*-coding=utf8 -*-
from math import sqrt as sqrt
import time

"""
========================
Project Euler Problem 03
========================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""


def check_prime(n):
    if n==2:
        return True
    if n%2==0:
        return False
    for i in xrange(3, int(sqrt(n)+1),2):
        if float(n)/i%1==0:
            return False
	
    else:
        return True

def largest_prime(n):
	x=3
	while True:
		while not check_prime(x):
				x+=2		
		if n%x==0:
			n/=x
			x+=2			
		elif check_prime(n):
			return n
		else: x+=2

if __name__=='__main__':
    time1=time.time()
    print largest_prime(600851475143)
    time2=time.time()
    print time2-time1	
