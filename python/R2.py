
########
#link https://open.kattis.com/problems/r2
########


#We are given:
#s = (r1+r2)/2

#and asked to compute r2, which can be done as such:
#2s - r1


import sys

for i in sys.stdin:
	inp = i.split()

	r1 = int(inp[0])
	s = int(inp[1])

	r2 = 2*s-r1
	print(r2)



