#!/usr/bin/env python2
import time
time1=time.time()
def pythagorean():
    for a in xrange(500):
        for b in xrange(a+1,500):
                c=1000-(a+b)
                if a**2+b**2==c**2:
                    return a*b*c
                    
print pythagorean()
time2=time.time()
print time2-time1
