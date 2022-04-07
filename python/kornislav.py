########
#link https://open.kattis.com/problems/kornislav
########

inp = list(map(int, input().split()))

inp.sort()



res = inp[0] * inp[2]

print(res)
