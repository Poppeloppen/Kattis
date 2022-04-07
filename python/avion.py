########
#link https://open.kattis.com/problems/avion
########

FBI_check = []
for i in range(1, 6):
	check_for = 'FBI'

	string = input()
	
	if check_for in string:
		FBI_check.append(i)

if len(FBI_check) < 1:
	print('HE GOT AWAY!')

else:
	print(*FBI_check)