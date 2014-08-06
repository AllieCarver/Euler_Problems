import math
def factors(n):
	factors=[]
	for i in xrange(1,int(math.sqrt(n))+1):
		if (float(n)/i)%1==0:
			factors.append(i)	
	for i in list(factors)[::-1]:
		if n/i < n:
		    factors.append(n/i)
	return factors


def amicable_sum():
    amicable=set([])
    for i in range(10001):
        if i==sum(factors(sum(factors(i)))) and i!=sum(factors(i)):
            amicable.add(i)
            amicable.add(sum(factors(i)))
    return sum(amicable)            

print amicable_sum()
