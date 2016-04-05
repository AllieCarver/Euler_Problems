#!-*-coding=utf8 -*-

import time


"""
========================
Project Euler Problem 63 
========================

The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

"""

def problem63():
    n = 0
    for i in xrange(1,100):
        for j in xrange(1,100):
            k = str(i**j)
            if len(k)==j:
                n+=1
            
    return n


if __name__ == '__main__':        
    time1=time.time()
    print problem63()
    time2=time.time()
    print time2-time1
