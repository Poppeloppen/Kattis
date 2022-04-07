########
#link https://open.kattis.com/problems/ladder
########

import math

a, A = list(map(int, input().split())) #Get the length of the triangle a, and the opposing angle A

B = 90 #We know the angle B is 90degrees


#to calculate the sidelength of b, the following formula is used
b = a * math.sin(math.radians(B)) / math.sin(math.radians(A))

print(math.ceil(b))

