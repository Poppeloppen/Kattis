########
#link https://open.kattis.com/problems/nastyhacks
########

cases = int(input())



for i in range(cases):
	numbers = list(map(int, input().split()))
	#print(numbers)

	expected_no_ad = numbers[0]
	expected_w_ad = numbers[1]
	cost = numbers[2]

	profit_w_ad = expected_w_ad - cost

	#print(f'profit_w_ad: {profit_w_ad}')

	if expected_no_ad < profit_w_ad:
		print('advertise')

	elif expected_no_ad == profit_w_ad:
		print('does not matter')

	else:
		print('do not advertise')

