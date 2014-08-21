#!-*-coding=utf8 -*-

import time

"""
========================
Project Euler Problem 31
========================

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

"""
def problem31():
    count=2
    pound2=[0,200]
    pound1=[0,100]
    pence50=[i*50 for i in xrange(5)]
    pence20=[i*20 for i in xrange(11)]
    pence10=[i*10 for i in xrange(21)]
    pence5=[i*5 for i in xrange(41)]
    pence2=[i*2 for i in xrange(101)]
    pence1=[i for i in xrange(201)]
    
    for l1 in pound1:
        for p50 in pence50:
            if l1+p50>200:
                break
            for p20 in pence20:
                if l1+p50+p20>200:
                    break
                for p10 in pence10:
                    if l1+p50+p20+p10>200:
                        break
                    for p5 in pence5:
                        if l1+p50+p20+p10+p5 >200:
                            break
                        for p2 in pence2:
                            if l1+p50+p20+p10+p5+p2 >200:
                                break
                            for p in pence1:
                                if l1+p50+p20+p10+p5+p2+p==200:
                                    count+=1
                                if l1+p50+p20+p10+p5+p2+p > 200:
                                    break
    return count

if __name__=='__main__':
    time1=time.time()
    print problem31()
    time2=time.time()
    print time2-time1
