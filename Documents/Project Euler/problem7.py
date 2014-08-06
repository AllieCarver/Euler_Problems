#!/usr/bin/env python2
import math
def check_prime(n):
	factors=[]
	for i in xrange(2, int(math.sqrt(n))+1):
			if float(n)/i%1==0:
			
				factors.extend([i])
	if len(factors) is 0:
		return True
	else:
		return False
def question7():
	x=2
	y=0
	while y < 10001:
		if check_prime(x):
			y+=1
		if x==2:
			x+=1
		elif x >= 3:
			x+=2
	print x-2
question7()		
