########
#link https://open.kattis.com/problems/zyxab
########

# a b c d e f g h i j k l m n o p q r s t u v w x y z




# max_iterations = int(input())

# name = input()
# test_no = 1

# while test_no < max_iterations:

# 	letter_list = [char for char in name]
# 	alph_val_list = [ord(char)-96 for char in letter_list]
# 	print(alph_val_list)

# 	name = input()
	
# 	test_no += 1



#########
# 2nd attempt, just finds the total alphabetical value of all WORDS,
# then sort --> should sort letter wise
#########
# max_iterations = int(input())

# name_list = []
# name_dict = dict()
# for i in range(max_iterations):
# 	name = input()
# 	name_val = sum([ord(character)-96 for character in name])

# 	name_dict[name] = name_val

# print(name_dict)
	






#########
# 1st attempt, doesn't take into account that if two words have 
# the same alphabetical value, the shortest one should be selected
#########
# max_iterations = int(input())

# name_list = []
# for i in range(max_iterations):
# 	name_list.append(input())

# name_list.sort()
# #print(f'Full name list: {name_list}')

# last_element = name_list.pop()
# #print(f'First best name: {last_element}')

# test = 1
# while test < max_iterations:
# 	if len(last_element) >= 5 and len(set(last_element)) == len(last_element):
# 		print(last_element)
# 		break

# 	last_element = name_list.pop()
# 	#print(f'New best name: {last_element}')

# 	test += 1

# if not test < max_iterations:
# 	print("neibb!")
