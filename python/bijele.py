########
#link https://open.kattis.com/problems/bijele
########

inp = list(map(int, input().split()))

#Lookup table
true_dict = {'king': 1,
				'queen': 1,
				'rooks': 2,
				'bishops': 2,
				'knights': 2,
				'pawns': 8}


#print(true_dict)

#Iterate over input and true values
dif = []
for input, true in zip(inp, true_dict.values()):
	dif.append(true-input)

#Unpack elements of list when printing
print(*dif)

