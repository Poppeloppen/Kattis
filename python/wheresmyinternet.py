########
#link https://open.kattis.com/problems/wheresmyinternet
########

houses, cables = map(int, input().split())



connected_dict = {}
connected_dict['Connected'] = list(map(int, input().split()))





for i in range(cables-1):
	
	house_1, house_2 = map(int, input().split())

	if house_1 in connected_dict['Connected'] or house_2 in connected_dict['Connected']:  # or house_2
		
		connected_dict['Connected'] = connected_dict['Connected'] + [house_1, house_2]

	else:
		connected_dict['Dis-connected'] = [house_1, house_2]




print(connected_dict)