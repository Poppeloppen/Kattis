########
#link https://open.kattis.com/problems/shatteredcake
########

width = int(input())

n = int(input())

total_area = 0
for i in range(n):
    w, l = list(map(int, input().split()))
    area = w * l

    total_area += area


length = total_area//width

print(length)
