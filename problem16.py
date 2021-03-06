#!-*-coding=utf8 -*-

import time

"""
========================
Project Euler Problem 16
========================
1**5 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""
def problem16():
    return sum([int(i)for i in list(str(long(2**1000)))])

if __name__=='__main__':
    time1=time.time()
    print problem16()
    time2=time.time()
    print time2-time1
