string = input()


for i in range(len(string)):
	if string[i] == ':' or string[i] == ';':

		try:
			if string[i+1] == ')':
				print(i)

			elif string[i+1] == '-' and string[i+2] == ')':
				print(i)

		except:
			break




#This code counts the number of occurences of each emoji, not what we want...
# emojis = {
# 	'emoji1': ':)',
# 	'emoji2': ';)',
# 	'emoji3': ':-)',
# 	'emoji4': ';-)'
# }

# emoji_cnt = 0
# for k, v in emojis.items():
	
# 	emoji_cnt += string.count(v)
# 	print(emoji_cnt)

# print(emoji_cnt)