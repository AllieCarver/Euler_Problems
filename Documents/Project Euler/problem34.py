"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
import math
import time

def problem34():
    total=0
    factorials={}
    for i in xrange(10):
        factorials[str(i)]=math.factorial(i)    
    for i in xrange(3,50000):
        factorial_sum=0
        for j in str(i):
            factorial_sum+=factorials[j]
        if factorial_sum==i:
            total+=factorial_sum
    return total
time1=time.time()
print problem34()
time2=time.time()
print time2-time1
