########
#link https://open.kattis.com/problems/thisaintyourgrandpascheckerboard
########

import numpy as np

n = int(input())


matrix = []

for i in range(n):
	row = [char for char in input()]

	matrix.append(row)

print(matrix)

