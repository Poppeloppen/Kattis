########
#link https://open.kattis.com/problems/qaly
########


inp = int(input())

counter = 0

for i in range(inp):
	q,y = map(float, input().split())

	counter += q*y


print(counter)





