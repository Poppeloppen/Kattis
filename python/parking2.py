########
#link https://open.kattis.com/problems/parking2
########

n = int(input())

for i in range(n):
    no_stores = int(input())
    stores = list(map(int, input().split()))

    min_store = min(stores)
    max_store = max(stores)

    final = 2*(max_store - min_store)
    print(final)
