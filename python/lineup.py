########
#link https://open.kattis.com/problems/lineup
########

n = int(input())


name_list = []
for _ in range(n):
	name = input()
	name_list.append(name)


if name_list == sorted(name_list, reverse = True):
	print('DECREASING')

elif name_list == sorted(name_list):
	print('INCREASING')

else:
	print('NEITHER')