#!-*-coding=utf8 -*-

import time
from itertools import permutations 


"""
========================
Project Euler Problem 
========================
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104
(3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has
exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are
cube.
"""

def is_cubic(n):
    if str(n**(float(1)/3)).split('.')[-1]=='0':
        return True
    return False	

def problem62():
    i = 1032
    while True:
        i += 1 
        print i
        cube = str(i **3)
        count = 0
        cube_set = set([])
        for perm in permutations(cube, len(cube)):
            if perm[0] != '0':
                pnum = "".join(perm)
                if is_cubic(int(pnum)):
                    if len(str(int(pnum)))==len(perm):
                        cube_set.add(pnum)
        if len(cube_set) ==5:
            return min(cube_set), cube_set

if __name__ == '__main__':        
    time1=time.time()
    print problem62()
    time2=time.time()
    print time2-time1
