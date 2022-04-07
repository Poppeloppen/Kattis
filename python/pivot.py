# to profile use following command when running the code: kernprof -l -v pivot.py < 1.in
# uhh, and remember uncommenting the @profile line
# link to source: https://github.com/pyutils/line_profiler



#Total old time: 0.000144 s on 1.in
#Total old time: 0.000144 s on 2.in



#Total old time: 0.000144 s on 1.in

@profile
def pivot_finder():

	n = input()

	array = list(map(int, input().strip().split()))
			

	pivot_cnt = 0

	for idx in range(int(n)): #check if each of the numbers could be a pivot
		
		a2 = array #copy the original array
		
		before = a2[:idx] #create new array with all the values that is before the pivor

		after = a2[idx+1:] #create a new array with all the values that is after the pivot
		

		potential_pivot = a2[idx]

		before.sort()
		after.sort()


		b_check = len(before)==0 or before[-1] < potential_pivot

		a_check = len(after)==0 or after[0] > potential_pivot


		if b_check and a_check: 
			pivot_cnt += 1


	return(pivot_cnt)


print(pivot_finder())

















# @profile
# def pivot_finder():

# 	n = input()

# 	array = list(map(int, input().strip().split()))
			

# 	pivot_cnt = 0

# 	for idx in range(int(n)): #check if each of the numbers could be a pivot
		
# 		a2 = array #copy the original array
		
# 		before = a2[:idx] #create new array with all the values that is before the pivor

# 		after = a2[idx+1:] #create a new array with all the values that is after the pivot
		

# 		potential_pivot = a2[idx]

# 		b_check = all(i <= potential_pivot for i in before) #check if all values in `before` array is less than the pivot

# 		a_check = all(i >= potential_pivot for i in after) #check if all values in `after` array is less than the pivot


# 		if b_check and a_check: 
# 			pivot_cnt += 1


# 	return(pivot_cnt)