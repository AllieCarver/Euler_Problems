#!/usr/bin/env python2
import math
def factors(n):
    factors=[]
    if n%2==0:
        step=1
    else: step=2
    for i in xrange(1,int(math.sqrt(n))+1,step):
        if (float(n)/i)%1==0:
            factors.append(i)
    for i in list(factors)[::-1]:
        factors.append(n/i)
    return len(factors)
def trianglenum():
    i=1
    n=i
    while True:
        if factors(n)>500:
            return n
        else:
            i+=1
            n+=i
print trianglenum()
