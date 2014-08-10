#!-*-coding=utf8 -*-
import math
import time

"""
========================
Project Euler Problem 46
========================
It was proposed by Christian Goldbach that every odd composite number 
can be written as the sum of a prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as 
the sum of a prime and twice a square?"
"""


def prime(n):
    if n==2:
        return True
    if n==0 or n==1:
        return False
    for i in xrange(2,int(math.sqrt(n))+1):
        if float(n)%i==0:
            return False
    return True


def problem46():
    n=33
    answer=None
    while True:
        if not prime(n):
            i=1
            good=True
            while good:
                square = 2*i**2
                if n - square<=0:
                    return n
                    
                elif prime(n-square):
                    good=False
                i+=1            
        n+=2            

if __name__=='__main__':
    time1=time.time()
    print problem46()
    time2=time.time()
    print time2-time1	

