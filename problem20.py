import math
def factorial(n):
    factorial=str(math.factorial(n))
    factorial_sum=0
    for i in factorial:
        factorial_sum+=int(i)
    return factorial_sum
print factorial(100)
