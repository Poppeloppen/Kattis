########
#link https://open.kattis.com/problems/cd
########

from sys import stdin


##### NOTE THE WHILE LOOP --> this is done since the input consists of a
# SEQUENCE of test cases
while True:

	n, m = list(map(int, stdin.readline().split()))

	if n == 0 and m == 0:
		break

	jacks_records = set()
	for record in range(n):
		jacks_records.add(stdin.readline())


	duplicates = 0
	for record in range(m):
		if stdin.readline() in jacks_records: #the IN operator is the part that takes a long time (avg. O(N) for lists, avg O(1) for set/dict -> worst case O(N))
			duplicates += 1




	print(duplicates)