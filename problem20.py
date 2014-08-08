#!-*-coding=utf8 -*-
import math
import time

"""
========================
Project Euler Problem 20
========================

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""
	
def problem20(n):
    factorial=str(math.factorial(n))
    factorial_sum=0
    for i in factorial:
        factorial_sum+=int(i)
    return factorial_sum

if __name__=='__main__':
    time1=time.time()
    print problem20(100)
    time2=time.time()
    print time2-time1
