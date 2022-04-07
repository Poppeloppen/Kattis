########
#link https://open.kattis.com/problems/speedlimit
########

while True:
	n = int(input())

	if n == -1:
		break


	previous_time = 0
	speeds = []
	times = []
	for i in range(n):
		speed, time = list(map(int, input().split()))
		speeds.append(speed)

		times.append(time-previous_time)


		previous_time = time


	total_dist = 0
	for time, speed in zip(speeds, times):
		total_dist += time*speed


	print(total_dist, 'miles')