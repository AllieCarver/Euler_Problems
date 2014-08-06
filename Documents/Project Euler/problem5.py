#!/usr/bin/env python2
def multiples():
    x=20
    done=False
    while not done:
        count=0
        if x%19==0:    
            for i in xrange(1,21):
                if x%i==0:
                    count+=1
                else: break
        if count==20:
            done=True
        else:
            x+=20
      
    print x
multiples()

