########
#link https://open.kattis.com/problems/helpaphd
########


import sys

lines = sys.stdin.readlines()
list_of_lists =  [line.split() for line in lines]

list_of_str = list(map(''.join, list_of_lists))


for i in list_of_str[1:]:
	if i[0] == 'P':
		print('skipped')
	else:
		#result = int(i[0])+int(i[-1])
		#Locate the '+' sign
		plus_idx = i.find('+')

		#The number before the '+'
		a = i[plus_idx+1:]

		#The number after the '+'
		b = i[0:plus_idx]

		result = int(a)+int(b)
		print(result)


