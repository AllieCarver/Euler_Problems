#!/usr/bin/env python2
#!-*-coding=utf8 -*-

import time

"""
========================
Project Euler Problem 01
========================

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

def problem01():
    x=set([])
    for i in range(1000):
	    if i % 3 == 0 or i % 5  == 0:
			    x.add(i)	
    return sum(x) 

if __name__=='__main__':
    time1=time.time()
    print problem01()
    time2=time.time()
    print time2-time1	

