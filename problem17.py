#!-*-coding=utf8 -*-

import time

"""
========================
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there 

are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 

how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters 

and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
def problem17(): 
    values_under_twenty={'':0,'00':0, '0':0, '1':3, '2':3, '3':len('three'),'4':len('four'),'5':len('five'),'6':len('six'),'7':len('seven'),'8':len('eight'),'9':len('nine'),'10':len('ten'),'11':len('eleven'),'12':len('twelve'),'13':len('thirteen'),'14':len('fourteen'),'15':len('fifteen'),'16':len('sixteen'),'17':len("seventeen"),'18':len('eighteen'),'19':len('nineteen')}
    tens_values={'2':len('twenty'),'3':len('thirty'),'4':len('forty'),'5':len('fifty'),'6':len('sixty'),'7':len('seventy'),'8':len('eighty'),'9':len('ninety')}
    letters=0
    for i in xrange(1001):
   
        if int(str(i)[-2:])<20:
            letters+=values_under_twenty[str(i)[-2:].lstrip('0')]
        else:
        
            letters+=(tens_values[str(i)[-2]]+values_under_twenty[str(i)[-1]])
        if 1000> i > 99:
            if int(str(i)[-2:])==0:
                letters+=(values_under_twenty[str(i)[-3]]+len('hundred'))
            else:
                letters+=(values_under_twenty[str(i)[-3]]+len('hundredand'))
        if i == 1000:
            letters+=11
    return letters        

if __name__=='__main__':
    time1=time.time()
    print problem17()
    time2=time.time()
    print time2-time1	
