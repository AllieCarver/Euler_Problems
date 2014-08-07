#!/usr/bin/env python2
#!-*-coding=utf8 -*-

import time

"""
========================
Project Euler Problem 09
========================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

def pythagorean():
    for a in xrange(500):
        for b in xrange(a+1,500):
                c=1000-(a+b)
                if a**2+b**2==c**2:
                    return a*b*c
                    
if __name__=='__main__':
    time1=time.time()
    print pythagorean()
    time2=time.time()
    print time2-time1	

