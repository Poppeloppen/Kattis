########
#link https://open.kattis.com/problems/sevenwonders
########

t = 0
c = 0
g = 0

for i in input():
	if i == 'T':
		t += 1

	elif i == 'C':
		c += 1

	else:
		g += 1

total = t**2 + c**2 + g**2 + min(t, c, g)*7

print(total)