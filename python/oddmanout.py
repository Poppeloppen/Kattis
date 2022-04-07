########
#link https://open.kattis.com/problems/oddmanout
########

from collections import Counter

cases = int(input())

for idx,i in enumerate(range(cases)):
	no_of_guests = int(input())

	guest_list = list(map(int, input().split()))

	c = Counter(guest_list)

	for j in c.keys():
		if c[j] == 1:
			print(f'Case #{i+1}: {j}')


	

