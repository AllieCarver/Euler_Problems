#!-*-coding=utf8 -*-

import time

"""
========================
Project Euler Problem 15
========================


Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there 

are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

"""
	
def problem15():
    row=[1 for i in range(21)]
    for i in xrange(20):
        next_row=[1]
        for i in row[1:]:
            next_row.append(i+next_row[row.index(i)-1])
        row=next_row
    return row[-1]

if __name__=='__main__':
    time1=time.time()
    print problem15()
    time2=time.time()
    print time2-time1
