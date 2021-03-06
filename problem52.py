#!-*-coding=utf8 -*-

import time


"""
========================
Project Euler Problem 52
========================

It can be seen that the number, 125874, and its double, 251748, contain 

exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,

 contain the same digits.

"""
def problem52():
    n=1
    while True:
        if (set(str(n)).difference(set(str(n*6))) 
            or set(str(n)).difference(set(str(n*5))) 
            or set(str(n)).difference(set(str(n*4)))
            or set(str(n)).difference(set(str(n*3))) 
            or set(str(n)).difference(set(str(n*2)))):
                n+=1
        elif len(set(str(n))) != len(list(str(n*6))):
            n+=1
        else:
            return n 

if __name__=="__main__":
    time1=time.time()
    print problem52()
    time2=time.time()
    print time2-time1           

