from itertools import permutations
x = [0,1,2,3,4]

y = permutations(x,2)
count = 0
for i in y:
    count+=1
    print i
    print count
