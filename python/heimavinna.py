########
#link https://open.kattis.com/problems/heimavinna
########

inp = input().replace(" ","").split(';')

num_tasks = 0
for i in inp:
    if ('-' in i):
        task1, task2 = list(map(int, i.split('-')))
        num_tasks += task2-task1+1
    else:
        num_tasks += 1

print(num_tasks)




