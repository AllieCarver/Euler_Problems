"""

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
days_in_month={'Jan':31,'Feb':28,'Leap':29,'Mar':31,'Apr':30,'May':31,'Jun':30, 'Jul':31, 'Aug':31, 'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}
months=['Jan', 'Feb','Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
weekday={0:'Mon', 1:'Tue', 2:'Wed', 3:'Thur', 4:'Fri', 5:'Sat', 6:'Sun'}
year=1901
current_day=1
sundays=0
done=False
while not done:
    for month in months:
        if done:
            break
        length_of_month=days_in_month[month]
        if month=='Feb':    
            if year%4==0 and year%100!=0:
                length_of_month+=1
            if year%400==0:
                length_of_month+=1
        for day in xrange(length_of_month):
            if month=='Dec' and year==2000 and day==30:
                if year==2000 and day==30:
                        done=True
                        break
            if day==0 and weekday[current_day%7]=='Sun':
                sundays+=1
            current_day+=1  
    if not done:year+=1  
print weekday[current_day%7],year, sundays
             
    

