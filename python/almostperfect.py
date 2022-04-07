########
#link https://open.kattis.com/problems/almostperfect
########

import math


def perfect(p: int) -> int:
	l = 1
	for i in range(2, int(math.sqrt(p)) + 1):
		if p % i == 0:
			l += i

			if i < math.sqrt(p):
				l += (p // i)


	if l == p:
		return f'{p} perfect'

	elif l - 2 <= p <= l + 2 and l != p:
		return f'{p} almost perfect'

	else:
		return f'{p} not perfect'

###
# This way of running the function was what made the final difference - modified function did not work
# with the inital method from 1st attempt
###
while True:
	try :
		n = int(input())
		print(perfect2(n))
	except EOFError:
		break


######
# 1st try did not work (Time limit exceeded)
######

# def perfect(p: int) -> int:
# 	divisors = []
# 	for i in range(1, p):
# 		if p % i == 0:
# 			divisors.append(i)

# 	sum_divisors = sum(divisors)
	
# 	if sum_divisors == p:
# 		return f'{p} perfect'

# 	elif sum_divisors - 2 <= p <= sum_divisors + 2 and sum_divisors != p:
# 		return f'{p} almost perfect'

# 	else:
# 		return f'{p} not perfect'


# while True:
# 	line = input()
# 	if len(line) < 1:
# 		break
# 	print(perfect(int(line)))
	