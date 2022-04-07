########
#link https://open.kattis.com/problems/statistics
########



import sys

list_of_lists = []

for line in sys.stdin:
	l = [int(elm) for elm in line.split()]
	list_of_lists.append(l)



for i in range(len(list_of_lists)):
	minimum = min(list_of_lists[i][1:])
	maximum = max(list_of_lists[i][1:])
	range = maximum - minimum

	print(f'Case {i+1}:', minimum, maximum, range)

