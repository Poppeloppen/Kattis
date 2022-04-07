########
#link https://open.kattis.com/problems/pot
########

import sys

lines = sys.stdin.readlines()

list_of_lists = [line.split() for line in lines]


#transform input to list_of_str
list_of_str = list(map(''.join, list_of_lists))

list_of_new_numbers = []
for element in list_of_str[1:]:
	power =int(element[-1])
	number = int(element[:-1])
	list_of_new_numbers.append(number**power)

result = sum(list_of_new_numbers)
print(result)











