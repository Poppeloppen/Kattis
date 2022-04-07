########
#link https://open.kattis.com/problems/spavanac
########

hours, minutes = list(map(int, input().split()))

if minutes >= 45:
	minutes -= 45



elif hours == 0:
	hours = 23

	minutes = 60 - (45-minutes)


else:
	hours -= 1

	minutes = 60 - (45-minutes)




print(hours, minutes)
