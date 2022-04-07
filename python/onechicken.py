########
#link https://open.kattis.com/problems/onechicken
########

people, chicken = input().split()

people, chicken = int(people), int(chicken)


leftover = chicken - people


if leftover > 0 and leftover == 1:
	print(f'Dr. Chaz will have {leftover} piece of chicken left over!')

elif leftover > 0:
	print(f'Dr. Chaz will have {leftover} pieces of chicken left over!')

elif leftover < 0 and leftover == -1:
	print(f'Dr. Chaz needs {abs(leftover)} more piece of chicken!')

else:
	print(f'Dr. Chaz needs {abs(leftover)} more pieces of chicken!')
