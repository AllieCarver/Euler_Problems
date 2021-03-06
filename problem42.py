# -*- coding: utf-8 -*-
     
import string
import time

"""
========================
Project Euler Problem 42
========================
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values 

we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle 

number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English 

words, how many are triangle words?


"""

with open('./Downloads/words.txt') as data:
    words=data.readline().split('","')
    words[0]=words[0].strip('"')
    words[-1]=words[-1].strip('"')

def alphabet_values():
    alphabet={}
    value=1
    for i in string.ascii_uppercase:
        alphabet[i]=value
        value+=1
    return alphabet


values=alphabet_values()


def char_sum(word):
    total=int()
    for char in word:
        total+=values[char]
    return total

def problem42():
    triangle_nums=set([0])
    n=1
    count=int()
    while max(triangle_nums)<365:
        triangle_nums.add(n*(n+1)/2)
        n+=1
    for word in words:
        if  char_sum(word) in triangle_nums:
            count+=1    
    return count

if __name__=='__main__':
    time1=time.time()
    print problem42()
    time2=time.time()
    print time2-time1	
