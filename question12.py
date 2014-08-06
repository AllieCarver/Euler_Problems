#!/usr/bin/env python2
import math
def factors(n):
    factors=[]
    for i in xrange(1,int(math.sqrt(n))+1):
        if (float(n)/i)%1==0:
            factors.append(i)
    for i in list(factors)[::-1]:
        factors.append(n/i)
    return len(factors)
def trianglenum():
    n=1
    countlist=[n]
    done=False
    while not done:
        if factors(sum(countlist))>500:
            done=True
        else:
            n+=1
            countlist.append(n)
    print sum(countlist),countlist[-1]
trianglenum()
