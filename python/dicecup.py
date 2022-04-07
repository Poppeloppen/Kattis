########
#link https://open.kattis.com/problems/dicecup
########
from collections import Counter

dice = list(map(int, input().split()))

#print(dice)


sums = []
for i in range(1, dice[0]+1):
	for j in range(1, dice[1]+1):
		sums.append(i + j)

sums_dict = Counter(sums)


#Get max value
max_val = max(sums_dict.values())


#Iterate over key value pairs in counter
for key, value in sums_dict.items():

	#everytime value == max_val, print corresponding key
	if value == max_val:
		print(key)


#Get (and print) key with the highest value
#print(max(sums_dict, key=sums_dict.get))