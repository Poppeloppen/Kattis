########
#link https://open.kattis.com/problems/everywhere
########

cases = int(input())

for i in range(cases):
	trips = int(input())

	cities = set()
	for i in range(trips):
		cities.add(input())

	print(len(cities))