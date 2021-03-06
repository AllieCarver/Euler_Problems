#!-*-coding=utf8 -*-

import math
import time

"""
========================
Project Euler Problem 33
========================
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly
 believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits 
in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

def g_c_f(num,den):
    num_factors=set()
    den_factors=set()
    for i in xrange(1,int(math.sqrt(num))+1):
		if (float(num)/i)%1==0:
			num_factors.add(i)
    for i in list(num_factors)[::-1]:
		num_factors.add(num/i)
    for i in xrange(1,int(math.sqrt(den))+1):
		if (float(den)/i)%1==0:
			den_factors.add(i)
    for i in list(den_factors)[::-1]:
		den_factors.add(den/i)
    common=[i for i in den_factors if i in num_factors]
    return max(common)

def problem33():
    numerator=1
    denominator=1
    for i in xrange(10,100):
        for j in xrange(i+1,100):
            if i %10 != 0 and j % 10 != 0:
                if str(i)[0] in str(j) or str(i)[1] in str(j):
                    if str(i)[0] in str(j):
                        temp_i=list(str(i))
                        temp_i.remove(str(i)[0])
                        temp_j=list(str(j))
                        temp_j.remove(str(i)[0])
                        if float(temp_i[0]) / int(temp_j[0])==float(i)/j:
                            numerator*=int(temp_i[0])
                            denominator*=int(temp_j[0])
                    else:
                        temp_i=list(str(i))
                        temp_i.remove(str(i)[1])
                        temp_j=list(str(j))
                        temp_j.remove(str(i)[1])
                        if float(temp_i[0]) / int(temp_j[0])==float(i)/j:
                            numerator*=int(temp_i[0])
                            denominator*=int(temp_j[0])
    return denominator/g_c_f(numerator,denominator)

if __name__=='__main__':
    time1=time.time()
    print problem33()
    time2=time.time()
    print time2-time1	
