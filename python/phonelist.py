from sys import stdin


#@profile
def is_phonelist_consistent():

	number_of_phonenumbers = int(stdin.readline()) #Get the total number of phonenumbers


	dict_of_phonenumbers = {stdin.readline().strip():True} # add the first number to the set of phonenumbers
	#print(dict_of_phonenumbers.keys())
	for _ in range(number_of_phonenumbers-1): #Iterate over all the phonenumbers
		phonenumber = stdin.readline() #Get the phonenumber

		for number, _ in dict_of_phonenumbers.items():

			length_of_number = len(str(number))

			if phonenumber[0:length_of_number] == number:
				return 'NO'

		dict_of_phonenumbers[phonenumber] = True

	return 'YES'



#@profile
def main():
	number_of_tests = int(stdin.readline())

	for _ in range(number_of_tests):
		print(is_phonelist_consistent())


if __name__ == "__main__":
	main()
















