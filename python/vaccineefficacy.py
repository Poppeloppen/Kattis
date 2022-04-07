########
#link https://open.kattis.com/problems/vaccineefficacy
########


cases = int(input())

not_vaxed_dict = {'A': 0, 'B': 0, 'C': 0}
vaxed_dict = {'A': 0, 'B': 0, 'C': 0}

not_vaxed = 0 
vaxed = 0

for i in range(cases):
	patient = input()

	if patient[0] == 'N':
		for idx, i in enumerate(patient[1:]):
			
			if i == 'Y' and idx == 0:
				not_vaxed_dict['A'] += 1 

			if i == 'Y' and idx == 1:
				not_vaxed_dict['B'] += 1

			if i == 'Y' and idx == 2:
				not_vaxed_dict['C'] += 1

		not_vaxed += 1


	elif patient[0] == 'Y':
		for idx, i in enumerate(patient[1:]):
			
			if i == 'Y' and idx == 0:
				vaxed_dict['A'] += 1 

			if i == 'Y' and idx == 1:
				vaxed_dict['B'] += 1

			if i == 'Y' and idx == 2:
				vaxed_dict['C'] += 1

		vaxed += 1


cases = ['A', 'B', 'C']
for i in cases:
	
	start_perc = (not_vaxed_dict[i] / not_vaxed) * 100	
	end_perc = (vaxed_dict[i] / vaxed) * 100
	

	perc_decrease = ((start_perc -  end_perc) / start_perc) * 100


	#print(end_perc)

	if perc_decrease > 0:
		print(round(perc_decrease, 5))
	else:
		print('Not Effective')



		#not_vaxed_dict[]


