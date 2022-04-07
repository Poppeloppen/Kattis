########
#link https://open.kattis.com/problems/jackolanternjuxtaposition
########

import sys

inp = sys.stdin.readlines()

l = [int(i) for i in inp[0].split()]


sum = 1
for i in l:
	sum = sum*i

print(sum)