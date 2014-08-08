#!-*-coding=utf8 -*-

import time

"""
========================
Project Euler Problem 25
========================	
Find fist term in Fibonacci sequence with 1000 digits
"""

def fibonacci():
    fib=[1,1]
    while len(str(fib[-1]))<1000:
        x=sum(fib[-2:])
        fib.append(x)
    return fib.index(fib[-1])+1

if __name__=='__main__':
    time1=time.time()
    print fibonacci()
    time2=time.time()
    print time2-time1
