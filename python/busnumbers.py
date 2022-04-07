########
#link https://open.kattis.com/problems/busnumbers
########


no_of_bus_stops = int(input())

bus_stops = list(map(int, input().split()))

bus_stops.sort()



def get_consecutive_numbers(bus_stops):
	previous = 0
	list_of_neighbors = []

	for bus_num in bus_stops:
		
		if bus_num == previous+1:
			
			if bus_num-1 not in list_of_neighbors:
				list_of_neighbors.append(bus_num-1)
				list_of_neighbors.append(bus_num)
			else:
				list_of_neighbors.append(bus_num)

		previous = bus_num

	return list_of_neighbors



def output_correctly(consecutive_numbers):
	#[141, 142, 143, 174, 175]

	#Find the indices of where there is a jump (of more than 1) in numbers
	for idx, bus_num in enumerate(bus_stops):

		if bus_num == previous-1:
			continue
		else:
			


	return consecutive_numbers




consecutive_numbers = get_consecutive_numbers(bus_stops) # [141, 142, 143, 174, 175]




print(output_correctly(consecutive_numbers))












# previous = 0
# start = 0
# start_idx = 0
# current_last_idx = 0
# for idx, bus_num in enumerate(bus_stops):

# 	print(f'previous: {previous}, in iteration: {idx+1}')
# 	print(f'bus_num: {bus_num}, in iteration: {idx+1}')
	

# 	if bus_num == previous+1:
		
# 		print('idx:', idx)
# 		print('current_last_idx:', current_last_idx)

		
# 		start = bus_num-1
# 		start_idx = idx-1
	
# 		current_last_idx = idx


# 		print(bus_num)


# 	print('the first number of the short string', start)
# 	print('the index of the FIRST number of the short string', start_idx)
# 	print('the index of the LAST number of the short string', current_last_idx)

# 	previous = bus_num

# 	print('#'*20)





#print(bus_stops)













