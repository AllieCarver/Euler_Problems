#!-*-coding=utf8 -*-

import time
import math
"""
========================
Project Euler Problem 57
========================

It is possible to show that the square root of two can be                                              
expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5 
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the 
eighth expansion, 1393/985, is the first example where the number of
digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a 
numerator with more digits than denominator?
"""

def add1_findgcf(num,den):
    combined_num = (1 * den) + num
    combined_den = 1 * den
    return (combined_num, combined_den)

def add2_findgcf(num,den):
    combined_num = (2 * den) + num
    combined_den = 1 * den
    return (combined_num, combined_den)

def problem57():
    iteration = 2
    fraction = (7,5)
    con_frac = (5,2)
    count = 0
    while iteration < 1000:
        con_frac = add2_findgcf(con_frac[1], con_frac[0])
        fraction = add1_findgcf(con_frac[1], con_frac[0])
        if len(str(fraction[0])) > len(str(fraction[1])):
            count += 1
        iteration += 1    
    return count
 
if __name__=='__main__':
    time1=time.time()
    print problem57()
    time2=time.time()
    print time2-time1
