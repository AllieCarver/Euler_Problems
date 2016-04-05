#!-*-coding=utf8 -*-


import time


"""
========================
Project Euler Problem 56
========================

A googol (10**100) is a massive number: one followed by one-hundred zeros; 
100**100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

"""
def problem56():
    max_digital_sum=0
    for a in xrange(99,100):
        for b in xrange(95,100):
            test=sum([int(i) for i in str(a**b)])
            if test > max_digital_sum:
                max_digital_sum=test

    return max_digital_sum

if __name__=='__main__':
    time1=time.time()
    print problem56()
    time2=time.time()
    print time2-time1





