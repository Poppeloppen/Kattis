########
#link https://open.kattis.com/problems/reversebinary
########

inp = int(input())

org_binary = bin(inp)[2:]
reverse_binary = org_binary[::-1]

new_num = int(reverse_binary, 2)


print(new_num)