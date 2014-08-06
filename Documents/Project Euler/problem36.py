"""

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
import time
def problem36():
    total=0
    for i in xrange(1000000):
        if str(i)==str(i)[::-1]:
            if str(bin(i)).lstrip("0b")==str(bin(i)).lstrip("0b")[::-1]:
                total+=i
                     
    return total
    
    #Can also be written as the sum of a list comprehension
    
#    return sum([i for i in xrange(1000000)if str(i)==str(i)[::-1] and 
#        str(bin(i)).lstrip("0b")==str(bin(i)).lstrip("0b")[::-1]])
time1=time.time()    

#print problem36()

time2=time.time()

print time2-time1

def problem36b():
    palindromes=set()
    for a in xrange(10):
        palindromes.add(a)
        palindromes.add(int(str(a)+str(a)))
        for b in xrange(10):
            palindromes.add(int(str(a)+str(b)+str(a)))
            palindromes.add(int(str(a)+str(b)+str(b)+str(a)))
            for c in xrange(10):
                palindromes.add(int(str(a)+str(b)+str(c)+str(b)+str(a)))
                palindromes.add(int(str(a)+str(b)+str(c)+str(c)+str(b)+str(a)))
    for i in set(palindromes):
        if str(i)!=str(i)[::-1]:
            palindromes.discard(i)

        if str(bin(i)).lstrip("0b")!=str(bin(i)).lstrip("0b")[::-1]:
            palindromes.discard(i)
                        
    return sum(palindromes)

time3=time.time()

print problem36b()

time4=time.time()
print time4-time3

    
            
