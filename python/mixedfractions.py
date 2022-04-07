########
#link https://open.kattis.com/problems/mixedfractions
########


while True:
	numerator, denominator = list(map(int, input().split()))

	if numerator == 0 and denominator == 0:
		break

	whole_number = int(numerator/denominator)

	new_numerator = numerator % denominator
	
	print(f'{whole_number} {new_numerator} / {denominator}')