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

#def is_cubic(n):
#    if str(n**(float(1)/3)).split('.')[-1]=='0':
#        return True
#    return False	
def problem62():
    cubics = {}
    ans = []
    for i in xrange(9000):
        cube = str(i**3)
        cube_list = []
        for char in cube:
            cube_list += char
        cube_list.sort()
        cube_list = ''.join(cube_list)
        cubics[cube] = cube_list
    cubics_keys = cubics.keys()
    cubics_vals = cubics.values()
    for key in cubics_keys:
        val = cubics[key]
        if cubics_vals.count(val)==5:
            return key
            
    """
    i=3000
    while True:
        print i
        cube = str(i **3)
        count = 0
        perms = set(["".join(perm) for perm in permutations(cube, len(cube))])
        for perm in perms:
            if is_cubic(int(perm)):
                count += 1
        if count == 5:.; 
            return cube
        i-=1
    """
#or i in range(100):
#    print i**3
if __name__ == '__main__':        
    time1=time.time()
    print problem62()
    time2=time.time()
    print time2-time1
