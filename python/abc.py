########
#link https://open.kattis.com/problems/abc
########

inp = list(map(int, input().split()))

inp.sort()

a,b,c = inp



order = input()

correct_order_str = ""
for i in order:
	if correct_order_str != "":
		correct_order_str += " "

	if i == 'A':
		
		correct_order_str += str(a)
	elif i == 'B':
		#correct_order.append(inp[1])
		correct_order_str += str(b)
	else:
		#correct_order.append(inp[2])
		correct_order_str += str(c)

print(correct_order_str)







# labels = ['A', 'B', 'C']
# num_dict = {}
# for num, label in zip(inp, labels):
# 	# print(num, label)

# 	num_dict[label] = num




# string = ""
# order = input()
# for i in order:
# 	if i == 'A':
# 		string += f'{num_dict[labels[0]]} '
# 	elif i == 'B':
# 		string += f'{num_dict[labels[1]]} '
# 	elif i == 'C':
# 		string += f'{num_dict[labels[2]]} '


# print(string)



