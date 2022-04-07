########
#link https://open.kattis.com/problems/backspace
########

string = input()
char_list = [char for char in string]

final_list = []
for i in char_list:
	if i == '<':
		final_list.pop()
	else:
		final_list.append(i)



print(''.join(final_list))