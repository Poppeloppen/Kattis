########
#link https://open.kattis.com/problems/lastfactorialdigit
########

import sys
from math import factorial

lines = sys.stdin.readlines()

data = [line.split() for line in lines]
#print(data[1:])


for i in data[1:]:
	#convert from list of lists to list of strings
	# abd finally into a list of int
	emp_str = ''
	str = ''.join(i)
	num = int(str)


	fact = factorial(num)


	last_digit = fact % 10
	print(last_digit)


