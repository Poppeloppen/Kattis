########
#link https://open.kattis.com/problems/carrots
########

import sys

lines = sys.stdin.readlines() 



data = [line.split() for line in lines]


important_stuff = [int(i) for i in data[0]]

print(important_stuff[1])