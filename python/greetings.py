########
#link https://open.kattis.com/problems/greetings2
########

import sys


for line in sys.stdin:
	l = line.split()
	string = ''.join(l)
	
	#Find out how many e's are in the string input
	nr_e = len(string)-2

	#The e's outputtet
	nr_e2_0 = (nr_e * 2)*"e"
	

	#The final string:
	final = f"h{nr_e2_0}y"
	print(final)
