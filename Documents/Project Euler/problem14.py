def len_collatz():
    length=0
    longest=0
    for i in xrange(2,1000000):
        testlength=[]
        while i > 1:
            testlength.append(i)
            if i%2==0:
                i/=2
            else:
                i=3*i+1
        if len(testlength)>length:
            longest=testlength[0]
            length=len(testlength)
    print longest
len_collatz()
