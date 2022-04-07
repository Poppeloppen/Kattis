########
#link https://open.kattis.com/problems/anewalphabet
########

new_dict = {'a': '@',
	'b': '8',
	'c': '(',
	'd': '|)',
	'e': '3',
	'f': '#',
	'g': '6',
	'h': '[-]',
	'i': '|',
	'j': '_|',
	'k': '|<',
	'l': '1',
	'm': '[]\\/[]',
	'n': '[]\\[]',
	'o': '0',
	'p': '|D',
	'q': '(,)',
	'r': '|Z',
	's': '$',
	't': "']['",
	'u': '|_|',
	'v': '\\/',
	'w': '\\/\\/',
	'x': '}{',
	'y': '`/',
	'z': '2'
	}

sentence = input()


new_sentence = ""
for symbol in sentence:
	lower_case_symbol = symbol.lower()

	if lower_case_symbol in new_dict:
		new_sentence += new_dict[lower_case_symbol]
	else:
		new_sentence += symbol


print(new_sentence)