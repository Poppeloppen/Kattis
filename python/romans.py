########
#link https://open.kattis.com/problems/romans
########

x = float(input())

const = 1000*(5280/4854)

print(round(x * const))