""" Four different ways to read data from stdin
into list of lists """

#import sys
import sys

#Read in lines from stdin using readlines()
lines =  sys.stdin.readlines()



##########
#Method 1
##########

#Using a nested for-loop:


l = []
for idx, j in enumerate(lines):
	l.append([])

	for i in j.split():
		l[idx].append(int(i))
print(l)


##########
#Method 2
##########

#Using a for-loop with in combination of a list comprehension:


l2 = []
for j in lines:
	l2.append([int(i) for i in j.split()])
print(l2)




##########
#Method 3
##########

#Using a nested list comprehension:

l3 = [[int(i) for i in j.split()] for j in lines]
print(l3)





