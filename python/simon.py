########
#link https://open.kattis.com/problems/simon
########

cases = int(input())


for i in range(cases):
	
	sentence = input()
	
	if sentence.startswith('simon says'):
		com_str_2 = " ".join(sentence.split()[2:])
		print(com_str_2)
	else:
		print("\n")