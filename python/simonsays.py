########
#link https://open.kattis.com/problems/simonsays
########

import sys


lines = sys.stdin.readlines()


data = [[i for i in line.split()] for line in lines]
# data = [line.split() for line in lines]


for i in data[1:]:
	
	#print(i)
	if i[0] == 'Simon' and i[1] == 'says':
		string = ''.join(str(e)+" " for e in i[2:])

		print(string)
	else:
		continue

