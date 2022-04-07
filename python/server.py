########
#link https://open.kattis.com/problems/server
########

n, T = map(int, input().split())


tasks = list(map(int, input().split()))



cumul_time = 0
task = 0
for i in tasks:
	cumul_time += i
	task += 1
	
	if cumul_time > T:
		cumul_time -= i
		task -= 1	
		break
	

print(task)