#!-*-coding=utf8 -*-

import time

"""
========================
Project Euler Problem 48
========================

The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.

"""

def problem48():
    x=long()
    for i in xrange(1,1001):
        x+=i**i
    return str(x)[-10:]

time1=time.time()
print problem48()
time2=time.time()
print time2-time1    
        
