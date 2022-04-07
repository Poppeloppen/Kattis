n = int(input())

for i in range(n):
	inp = int(input())

	#print(inp // 400)
	#print(inp / 400)

	print(-(-inp // 400)) #Ceiling integer division (round up) source: https://stackoverflow.com/questions/14822184/is-there-a-ceiling-equivalent-of-operator-in-python