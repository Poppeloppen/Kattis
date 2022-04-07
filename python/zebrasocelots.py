########
#link https://open.kattis.com/problems/zebrasocelots
########

no_animals = int(input())


animal_list = []
for _ in range(no_animals):
	animal_list.append(input())

print(f'initial animal_list: {animal_list}')




while not all(x == 'z' for x in animal_list): #Returns true when all animals are zebras:
	
	#How many times have an ozelot been transformed to zebra
	transformations = 0

	#Pointer to keep track of where 
	pointer = 0 

	#Iterate over animal_list
	for idx, i in enumerate(reversed(animal_list)):
		
		#print(f'idx: {idx}')
		#print(f'i: {i}')

		#if we meet ozelot
		if i == 'o':
			#save pointer where we meet ozelot
			pointer = idx
			#print(pointer)

			#transform ozelot lowest in the pile to zebra (first in reversed list)
			animal_list[idx] = 'z'

			#transform all zebras to ozelots after the idx
			for num in range(len(animal_list[idx:])):
				print(animal_list[idx+num])


			

			#add 1 to transformations counter:
			transformations += 1

			print(animal_list[idx:])







# pointer = 0 
# for idx, i in enumerate(reversed(animal_list)):
	
# 	if i == 'o':
# 		pointer = idx


# 	print(idx, i)