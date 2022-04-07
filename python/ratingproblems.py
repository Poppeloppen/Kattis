########
#link https://open.kattis.com/problems/ratingproblems
########

inp = input().split()

judges, voted= int(inp[0]), int(inp[1])
yet_to_vote = judges - voted

constant = 0
for i in range(voted):
	constant += int(input())

#constant_score = constant




max = 0
min = 0
for i in range(yet_to_vote):
	max += 3
	min -= 3

max_score = (max + constant) / judges
min_score = (min + constant) / judges

print(min_score, max_score)


