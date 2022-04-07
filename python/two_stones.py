########
#link https://open.kattis.com/problems/twostones
########

import sys

for line in sys.stdin:
	inp = int(line)
	
	if inp % 2 == 0:
		print('Bob')
	else:
		print('Alice')

