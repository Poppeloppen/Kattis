########
#link https://open.kattis.com/problems/sumkindofproblem
########

no_of_datasets = int(input())

for i in range(no_of_datasets):
	k, n = list(map(int, input().split()))

	# print(k, n)



	pos_sum = sum([num for num in range(1, n+1)])
	odd_sum = sum([num for num in range(1, 2*n+1, 2)])
	even_sum = sum([num for num in range(2, 2*n+1, 2)])

	# print(odd_sum)
	print(k, pos_sum, odd_sum, even_sum)