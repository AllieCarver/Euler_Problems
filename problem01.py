#!/usr/bin/env python2
import time
time1=time.time()
x=set([])
for i in range(1000):
		
	if i % 3 == 0 or i % 5  == 0:
			x.add(i)	
print sum(x)
time2=time.time()
print time2-time1	
