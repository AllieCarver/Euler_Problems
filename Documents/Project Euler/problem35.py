"""

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import math
import time

def prime(n): 
	for i in xrange(2,int(math.sqrt(n))+2):
		if float(n)%i==0:
		    return False
	return True

def problem35():
    primes=set([i for i in range(3,1000000,2) if prime(i)])
    must_end_with='1379'
    for i in set(primes):
        for j in str(i):
            if int(j)%2==0 or int(j)%5==0:
                primes.discard(i)
                break
    for i in set(primes):
        temp_i=list(str(i))
        for j in xrange(len(str(i))):
            temp_i.append(temp_i.pop(0))
            if not prime(int("".join(temp_i))):
                primes.discard(i)
                break 
    #rather than treat 2 and 5 with special cases add it at the end of algorithm        
    primes.add(2)
    primes.add(5)            
    return len(primes)
time1=time.time()    
print problem35()
time2=time.time()
print time2-time1
