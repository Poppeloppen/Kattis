########
#link https://open.kattis.com/problems/plantingtrees
########

n = int(input())


trees = list(map(int, input().split()))

trees.sort(reverse = True)


number_of_days = 0
day_number = 1
for tree in trees:

	if tree + day_number > number_of_days:
		number_of_days = tree + day_number

	day_number += 1

print(number_of_days+1)