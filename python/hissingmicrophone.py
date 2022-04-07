########
#link https://open.kattis.com/problems/hissingmicrophone
########

data = input()

pointer = ""


hiss = False

for i in data:
	
	if i == pointer and (i =='s' or i == 'S'):
		hiss = True
		break


	pointer = i



if hiss == True:
	print('hiss')
else:
	print('no hiss')
