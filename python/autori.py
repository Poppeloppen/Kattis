########
#link https://open.kattis.com/problems/autori
########

name = [char for char in input()]

abr = [name[0]]
for i in range(len(name)):
	if name[i] == '-':
		abr.append(name[i+1])

print(''.join(abr))