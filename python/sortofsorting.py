########
#link https://open.kattis.com/problems/sortofsorting
########




while True:
	n = int(input())

	if n == 0:
		break


	names = []
	for i in range(n):
		name = input()
		names.append(name)


	names.sort(key = lambda name: name[:2]) #Sort only on the two first letters:

	for name in names:
		print(name)