########
#link https://open.kattis.com/problems/basicprogramming2
########

from collections import Counter


_, t = list(map(int, input().split()))

inp = list(map(int, input().split()))



def one(inp):

    table = set(inp)
  
    for x in inp:
        y = 7777 - x
        if x == y:
            continue

        if y in table:
            return 'Yes'

    return 'No'



def two(inp):
	if len(set(inp)) == len(inp):
		return 'Unique'
	else:
		return 'Contains duplicate'


def three(inp):
	counter = Counter(inp)

	for k,v in counter.items():
		if v > len(inp)/2:
			return k

	return -1


def four(inp):
	"""Return median of the inp, return two values in case of even input
	and a single number in case an uneven number
	"""

	inp.sort()

	center_idx = len(inp)/2


	if center_idx % 2 == 0:
		val1 = inp[int(center_idx)-1]
		val2 = inp[int(center_idx)]

		return f'{val1} {val2}'

	else:
		return inp[int(center_idx)]

def five(inp):
	
	valid_numbers = []

	inp.sort()

	for i in inp:
		if i >= 100 and i <= 999:
			valid_numbers.append(i)

	return valid_numbers
	



if t == 1:
	print(one(inp))

elif t == 2:
	print(two(inp))

elif t == 3:
	print(three(inp))

elif t == 4:
	print(four(inp))

elif t == 5:
	print(*five(inp), sep=' ')
