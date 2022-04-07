########
#link https://open.kattis.com/problems/filip
########

inp = input().split()
num1, num2 = int(inp[0][::-1]), int(inp[1][::-1]) #Reverse the two string inputs and convert to int

print(max(num2, num1)) 