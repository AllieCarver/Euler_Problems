#!/usr/bin/env python2
#!-*-coding=utf8 -*-

import time

"""
========================
Project Euler Problem 04
========================

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
	
def problem04():
	palindromes=set()
	for i in xrange(1,1000):
		for j in xrange(1,1000):
			x=str(i*j)
			if len(x) is 6:
				if x[0]==x[-1] and x[1]==x[-2] and x[2]==x[-3]:
					palindromes.add(int(x))
	return max(palindromes)

if __name__=='__main__':
    time1=time.time()
    print problem04()
    time2=time.time()
    print time2-time1
			
