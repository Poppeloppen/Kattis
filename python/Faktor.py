########
#link https://open.kattis.com/problems/faktor
########

import sys

lines = sys.stdin.readlines()

data = [[int(i) for i in line.split()] for line in lines]

data_list = data[0]


published, impact = data_list[0], data_list[1]


print(published * (impact - 1) + 1)




#875/38 = 23.04






#published * (impact - 1) + 1
