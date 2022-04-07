########
#link https://open.kattis.com/problems/pet
########

import sys

lines = sys.stdin.readlines()

data = [[int(i)for i in line.split()] for line in lines]



score_list = []
for i in data:
	score_list.append(sum(i))



highscore = max(score_list)
winner = score_list.index(highscore)+1

print(winner, highscore)


	
