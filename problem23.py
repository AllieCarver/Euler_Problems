import math
def abundant(n):
    factors=set([])
    for i in xrange(1,int(math.sqrt(n))+1):
		if n%i==0:
			factors.add(i)
    for i in set(factors):
            if n/i != n:
		        factors.add(n/i)   
    return sum(factors)>n

def not_abundant():
    abundant_nums=set([i for i in xrange(12,28123) if abundant(i)])
    not_abundant_sums=set(xrange(1,28123))
    abundant_sums=set([])
    for i in abundant_nums:
        for j in abundant_nums:
            if (i+j) < 28123:
                abundant_sums.add(i+j)
    return sum(not_abundant_sums.difference(abundant_sums))

print not_abundant()


