"""Find fist term in Fibonacci sequence with 1000 digits"""
def fibonacci():
    fib=[1,1]
    while len(str(fib[-1]))<1000:
        x=sum(fib[-2:])
        fib.append(x)
    return fib.index(fib[-1])+1
print fibonacci()
