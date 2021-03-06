#!-*-coding=utf8 -*-

import time

"""
========================
Project Euler Problem 39
========================
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

def problem39():
    p=int()
    largest=int()
    for i in xrange(12,1001):    
        count=int()
        for a in xrange(3,int(i/2)+1):
            for b in xrange(a+1,int(i/2)+1):        
                c=i-(a+b)
                if c > b:
                    if a**2+b**2==c**2:
                        count+=1
        if count>largest:
            largest=count
            p=i                        
                    
    return p, largest
if __name__=='__main__': 
    time1=time.time()                   
    print problem39()
    time2=time.time()
    print time2-time1
