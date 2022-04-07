########
#link https://open.kattis.com/problems/planina
########

iterations = int(input())



points_per_side = 2
for i in range(iterations):
	points_per_side += points_per_side -1 


print(points_per_side*points_per_side)