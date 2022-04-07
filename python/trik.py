########
#link https://open.kattis.com/problems/trik
########


inp = input()


ball = [1, 0, 0]
for i in inp:

	if i == 'A':
		ball[0], ball[1] = ball[1], ball[0]

	elif i == 'B':
		ball[1], ball[2] = ball[2], ball[1]

	else:
		ball[0], ball[2] = ball[2], ball[0]


if ball[0] == 1:
	print(1)

elif ball[1] == 1:
	print(2)

else:
	print(3)