########
#link https://open.kattis.com/problems/magictrick
########

inp = list(input())
inp_set = set(inp)

if len(inp) == len(inp_set):
    print(1)
else:
    print(0)
