########
#link https://open.kattis.com/problems/zoo
########





no_of_animals = int(input())

iteration = 1

while no_of_animals > 0:
	animal_dict = dict()
	uniq_animals = set()

	for i in range(no_of_animals):
		animal = list(input().split())[-1]
		

		if animal.lower() not in uniq_animals:
			uniq_animals.add(animal.lower())

			animal_dict[animal.lower()] = 1

		elif animal.lower() in uniq_animals:
			animal_dict[animal.lower()] += 1


	print(f'List {iteration}:')
	for k, v in sorted(animal_dict.items()):

		print(f'{k} | {v}')

	iteration += 1
	no_of_animals = int(input())


