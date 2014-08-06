import math
def check_prime(n):
	for i in xrange(2, int(math.sqrt(n)+1)):
		if float(n)/i%1==0:
			return False
	else:
		return True


def problem27():
    x=(0,0,0)
    b_list=[i for i in xrange(1,1001,2) if check_prime(i)]
    a_list=[i for i in xrange(-999,1001)]
    for a in a_list:
        for b in b_list:
            n=0
            while n**2 + a*n + b>=0 and check_prime(n**2 + a*n + b) :
                n+=1
            if n>x[0]:
                x=(n,a,b)
    return x, x[1]*x[2]
    
print problem27()
