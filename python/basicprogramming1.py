########
#link https://open.kattis.com/problems/basicprogramming1
########

def one():
	"""print 7 regardless of content of list"""
	return 7


def two(A: list) -> str:

	if A[0] > A[1]:
		return 'Bigger'

	elif A[0] == A[1]:
		return 'Equal'

	else:
		return 'Smaller'


def three(A: list) -> int:
	B = A[:3]
	B.sort()

	return B[1]


def four(A: list) -> int:
	return sum(A)


def five(A: list) -> int:
	even_list = []
	for i in A:
		if i % 2 == 0:
			even_list.append(i)

	return sum(even_list)


def six(A: list) -> str:
	alph_val = [i % 26 for i in A]

	letter_list = [chr(ord('a')+i) for i in alph_val]


	return ''.join(letter_list)


def seven(A: list) -> str:
	idx = 0
	loops_counter = 0

	while loops_counter < len(A):
		#print(idx)

		if idx >= len(A):
			return 'Out'

		elif idx == len(A) - 1:
			return 'Done'

		idx = A[idx]
		#print(idx)

		loops_counter += 1

	return 'cyclic'		


_, t = list(map(int, input().split()))

nums = list(map(int, input().split()))


if t == 1:
	print(one())

elif t == 2:
	print(two(nums))

elif t == 3:
	print(three(nums))

elif t == 4:	
	print(four(nums))

elif t == 5:
	print(five(nums))

elif t == 6:
	print(six(nums))

elif t == 7:
	print(seven(nums))


