########
#link https://open.kattis.com/problems/numberfun
########

cases = int(input())



for i in range(cases):
	numbers = list(map(int, input().split()))

	# print(numbers)


	if numbers[0] + numbers[1] == numbers[2] or numbers[1] + numbers[0] == numbers[2]:

		print('Possible')

	elif numbers[0] - numbers[1] == numbers[2] or numbers[1] - numbers[0] == numbers[2]:

		print('Possible')

	elif numbers[0] * numbers[1] == numbers[2] or numbers[1] * numbers[0] == numbers[2]:

		print('Possible')

	elif numbers[0] / numbers[1] == numbers[2] or numbers[1] / numbers[0] == numbers[2]:

		print('Possible')
		break

	else:
		print('Impossible')

