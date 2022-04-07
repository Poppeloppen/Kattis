########
#link https://open.kattis.com/problems/sorttwonumbers
########

inp = input().split()

data = [int(elm) for elm in inp]

data.sort()

print(data[0], data[1])