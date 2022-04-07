########
#link https://open.kattis.com/problems/mia
########

import sys

lines = sys.stdin.readlines()
list_of_lists = [line.split() for line in lines]
list_of_str = list(map(''.join, list_of_lists))

print(list_of_str[0])




# p1_score = ""
# p2_score = ""

# for i in list_of_str:
# 	player_1 = i[:2]
# 	player_2 = i[2:]

# 	#List of each players roll
# 	p1_roll = ([char for char in player_1])
# 	p2_roll = ([char for char in player_2])




# 	######
# 	#Score system
# 	######

# 	#Mia
# 	if p1_roll == ["2","1"] or p1_roll == ["1","2"]:
# 		p1_score = "mia"

# 	#Double
# 	elif p1_roll[0] == p1_roll[1]:
# 		p1_score = p1_roll[0]+p1_roll[0]

# 	#Normal
# 	else:
# 		if p1_roll[0] > p1_roll[1]:
# 			p1_score = p1_roll[0]+p1_roll[1]
# 		else:
# 			p1_score = p1_roll[1]+p1_roll[0]



# 	print(p1_score)


def player_roll(list_of_str):
	"""take in list of string len(4), 
	split the list into two seperate players"""
	for i in list_of_str:
		player_1 = i[:2]
		player_2 = i[2:]

		#List of each players roll
		p1_roll = ([char for char in player_1])
		p2_roll = ([char for char in player_2])

		return p1_roll, p2_roll




def score(l):
	"""Take in list with two number strings and calculate the score"""
	
	#If the score is mia, return very big number:
	if l == ["2","1"] or l == ["1","2"]:
		return 999999

	#Double diggits is better than regular numbers, add 2
	# extra 0's to ensure these values always is higher than
	# the regular rolls
	elif l[0] == l[1]:
		return int(l[0]+l[1]+'00')

	#Normal
	else:
		if l[0] > l[1]:
			return int(l[0]+l[1])
		else:
			return int(l[1]+l[0])



for i in list_of_str:

	print(i)
	p1_roll, p2_roll = player_roll(list_of_str)

	print(p1_roll)
	#print(i)
	# print(p1_roll)
	# print(p2_roll)

	##p1_score = score(p1_roll)
	##p2_score = score(p2_roll)

	#print(p1_score)
	#print(p2_score)


	# if p1_score == p2_score:
	# 	print('Tie.')
	# elif p1_score < p2_score:
	# 	print('Player 2 wins.')
	# else:
	# 	print('Player 1 wins.')





"""


Mia (12 or 21) is always highest.

Next come doubles (11, 22, and so on). Ties are broken by value, with 66 being highest.

All remaining rolls are sorted such that the highest number comes first, which results in a two-digit number. The value of the roll is the value of that number, e.g. 3 and 4 becomes 43.
"""