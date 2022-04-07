########
#link https://open.kattis.com/problems/cold
########

no_of_temps = int(input())




temps = input().split()

neg_temp = []
for i in temps:
	if int(i) < 0:
		neg_temp.append(int(i))

print(len(neg_temp))


