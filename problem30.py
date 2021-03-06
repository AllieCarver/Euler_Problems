#!-*-coding=utf8 -*-

import time

"""
========================
Project Euler Problem 30
========================
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1**4 + 6**4 + 3**4 + 4**4
    8208 = 8**4 + 2**4 + 0**4 + 8**4
    9474 = 9**4 + 4**4 + 7**4 + 4**4

As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
 
def problem30():
    total=0
    fifth_powers={}
    for i in xrange(10):
        fifth_powers[str(i)]=i**5
    upper_limit=10000
    while True:    
        current_total=0    
        for n in xrange(2,upper_limit):
            if sum([fifth_powers[i] for i in str(n)])==n:
                current_total+=n
            
        if current_total == total:
            return total
        else:
            total = current_total
            upper_limit *= 10

if __name__=='__main__':
    time1=time.time()
    print problem30()
    time2=time.time()
    print time2-time1	
