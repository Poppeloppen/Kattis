########
#link https://open.kattis.com/problems/aboveaverage
########

classes = int(input())

for i in range(classes):
	inp = list(map(int, input().split()))

	students = inp[0]
	grades = inp[1:]

	avg = sum(grades) // len(grades)

	abv_avg_perc = (len([num for num in grades if num > avg]) / len(grades)) * 100

	# print(students)
	# print(grades)
	# print(avg)
	print('{:.3f}%'.format(abv_avg_perc))