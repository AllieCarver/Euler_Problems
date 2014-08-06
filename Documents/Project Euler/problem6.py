#!/usr/bin/env python2
import time

def sumsquareb(n):
    global time1,time2
    time1=time.time()
    print (sum([i for i in xrange(n+1)]))**2-sum([i*i for i in xrange(n+1)]) 
    time2=time.time()
sumsquareb(int(raw_input('number')))

print time2-time1
