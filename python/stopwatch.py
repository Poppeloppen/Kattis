########
#link https://open.kattis.com/problems/stopwatch
########

presses = int(input())
is_running = False
accumaleted_time = 0
previous_time = 0

for _ in range(presses):
	current_time = int(input())
	if is_running:
		accumaleted_time += current_time - previous_time

	previous_time = current_time
	is_running = not is_running

if is_running:
	print('Still running')
else:
	print(accumaleted_time)





# press = 0
# print(f'press (start): {press}')


# if presses %2 != 0:
# 	print('still running')

# else:
# 	time = int(input())
# 	press += 1
# 	for i in range(presses-1):
# 		if press &2 == 0:
# 			time = int(input())
# 			press += 1
# 			print(f'press (even): {press}')
# 		else:
# 			time -= int(input())
# 			press += 1
# 			print(f'press (uneven): {press}')



# print(abs(time))