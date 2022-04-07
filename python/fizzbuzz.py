########
#link https://open.kattis.com/problems/fizzbuzz
########

inp = list(map(int, input().split()))

for i in range(1, inp[-1]+1):

	if i % inp[0] == 0 and i % inp[1] == 0:
		print('FizzBuzz')

	elif i % inp[0] == 0:
		print('Fizz')

	elif i % inp[1] == 0:
		print('Buzz')

	else:
		print(i)