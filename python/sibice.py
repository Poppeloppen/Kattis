########
#link https://open.kattis.com/problems/sibice
########
import math


n, height, width = list(map(int, input().split()))


#Pythagoras theorem
diagonal = math.sqrt(height**2 + width **2)

for _ in range(n):
	length_of_match = int(input())

	if length_of_match <= diagonal:
		print('DA')
	else:
		print('NE')
