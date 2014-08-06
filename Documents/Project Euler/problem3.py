#!/usr/bin/env python2
import math, time
def check_prime(n):
    if n==2:
        return True
    if n%2==0:
        return False
    for i in xrange(3, int(math.sqrt(n+1)),2):
        if float(n)/i%1==0:
            return False
	
    else:
        return True

def largest_prime(n):
	time1=time.time()
	done=False
	x=3
	while not done:
		while not check_prime(x):
				x+=2		
		if n%x==0:
			n/=x
			x+=2
			
		elif check_prime(n):
			done=True
			time2=time.time()
			
		else: x+=2
	print n
	print time2-time1
largest_prime(600851475143)
largest_prime(644)		
