#!-*-coding=utf8 -*-

import string
import re
import time

"""
========================
Project Euler Problem 22
========================

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""
	
def namelist():
    with open('./Downloads/names.txt') as data:
        namelist=list(data)
    namelist=namelist[0].split(',')
    for i in xrange(len(namelist)):
        namelist[i]=namelist[i].strip('"')
    namelist.sort()
    return namelist
    
def alphabet_values():
    alphabet={}
    value=1
    for i in string.ascii_uppercase:
        alphabet[i]=value
        value+=1
    return alphabet

def problem22():
    values=alphabet_values()
    names=namelist()
    total=0
    for name in names:
        total+=sum([values[char]for char in name])*(names.index(name)+1) 
    return total
  
if __name__=='__main__':
    time1=time.time()
    print problem22()
    time2=time.time()
    print time2-time1
