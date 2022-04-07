########
#link https://open.kattis.com/problems/modulo
########

uniq_num = set()

for i in range(10):
	num = int(input()) % 42

	uniq_num.add(num)

print(len(uniq_num))