########
#link https://open.kattis.com/problems/nodup
########

line = input().split()

unique = set(line)

if len(line) == len(unique):
	print('yes')

else:
	print('no')