########
#link https://open.kattis.com/problems/electricaloutlets
########

cases = int(input())



for i in range(cases):
	outlets = 0
	
	l = input().split()
	int_l = [int(elm) for elm in l]


	no_of_powerstrips = int_l[0]
	powerstips = int_l[1:]

	for i in powerstips[:-1]:
		outlets += i-1

	outlets += powerstips[-1]

	print(outlets)


