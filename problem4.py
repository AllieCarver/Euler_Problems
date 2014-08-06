#!/usr/bin/env python2
def palindrome():
	palindromes=[]
	for i in xrange(1,1000):
		for j in xrange(1,1000):
			x=str(i*j)
			if len(x) is 6:
				if x[0]==x[-1] and x[1]==x[-2] and x[2]==x[-3]:
					palindromes.append(int(x))
	print max(palindromes)
palindrome()
			
