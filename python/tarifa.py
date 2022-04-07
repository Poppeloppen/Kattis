########
#link https://open.kattis.com/problems/tarifa
########

data_availabel = int(input())

N = int(input())



data_availabel_next_month = data_availabel
for i in range(N):
	used = int(input())

	left = data_availabel_next_month - used
	
	data_availabel_next_month = left + data_availabel

print(data_availabel_next_month)

