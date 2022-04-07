########
#link https://open.kattis.com/problems/4thought
########

#We want string of all possible equations, by later using the eval() command we can get the solution
possible_equations = ['4']

for i in range(3):
	equations = []

	for string in possible_equations:
		equations.append(string+' + 4')
		equations.append(string+' - 4')
		equations.append(string+' * 4')
		equations.append(string+' / 4')

	possible_equations = equations


#Evaluate all the functions
solutions = {}
for equation in possible_equations:
	result = eval(equation)
	solutions[result] = equation




n = int(input())

for i in range(n):
	solution = int(input())

	if solution in solutions:
		s = solutions[solution]

		print(f'{s} = {solution}')
	else:
		print('no solution')







