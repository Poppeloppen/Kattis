########
#link https://open.kattis.com/problems/ofugsnuid
########


inp = int(input())

l = []
for _ in range(inp):
	l.append(int(input()))

l.reverse()

for i in l:
	print(i)
