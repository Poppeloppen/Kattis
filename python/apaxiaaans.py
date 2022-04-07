########
#link https://open.kattis.com/problems/apaxiaaans
########

name = input()


shortname = ''
previous_letter = ''
for letter in name:

	if letter == previous_letter:
		shortname += ''
	else:
		shortname += letter

	previous_letter = letter


print(shortname)
