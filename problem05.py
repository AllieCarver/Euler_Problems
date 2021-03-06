#!/usr/bin/env python2
#!-*-coding=utf8 -*-

import time

"""
========================
Project Euler Problem 05
========================

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
	
def problem05():
    x=20
    while True:
        count=0
        if x%19==0:    
            for i in xrange(1,21):
                if x%i==0:
                    count+=1
                else: break
        if count==20:
            return x
        else:
            x+=20
      
#    print x

if __name__=='__main__':
    time1=time.time()
    print problem05()
    time2=time.time()
    print time2-time1

