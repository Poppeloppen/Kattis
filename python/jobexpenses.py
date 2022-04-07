########
#link https://open.kattis.com/problems/zoo
########

n = int(input())

nums = list(map(int, input().split()))

exp = 0
for i in nums:
    if i < 0:
        exp += abs(i)


print(exp)
