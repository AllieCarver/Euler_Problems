import time
def check_prime(n):
    if n==2:
        return True
    if n%2==0:
        return False
    for i in xrange(3, int(math.sqrt(n)+1),2):
        if float(n)%i==0:
            return False	
    else:
        return True

def prime_factors_count(n):
    done=False
    factors=int()
    next_prime=3
    while True:
        if n%2==0:
            factors+=1
            while n%2==0:
                n/=2
            if check_prime(n):
                return factors
        
        while not (check_prime(next_prime) and n %next_prime==0) :
            next_prime+=2		        
        
        factors+=1
        
        while n %next_prime==0:
            n/=next_prime
                
        if check_prime(n):
            factors+=1
            return factors
        
        next_prime+=2

def ero_sieve(n):
    primes=set(i for i in xrange(3,n+1,2))
    for i in set(primes):
        j=2
        while i*j<n:
            primes.discard(i*j)
            j+=1 
    primes.add(2)
    return primes


