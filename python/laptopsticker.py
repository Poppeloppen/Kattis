########
#link https://open.kattis.com/problems/laptopsticker
########

inp = list(map(int,input().split()))


comp_x, comp_y = inp[0], inp[1]
stick_x, stick_y = inp[2], inp[3]

if stick_x <= comp_x-2 and stick_y <= comp_y-2:
	print(1)
else:
	print(0)