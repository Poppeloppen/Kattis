########
#link https://open.kattis.com/problems/jumbojavelin
########

n = int(input())

total_len = 0
for i in range(n):
    len = int(input())-1
    total_len += len

print(total_len+1)
