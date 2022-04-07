########
#link https://open.kattis.com/problems/teque
########
from sys import stdin


class Teque:
	def __init__(self):
		self.queue = []


	def push_back(self, num):
		"""push to back of que"""
		self.queue.append(num) 
		return 

	def push_front(self, num):
		"""push to front of que"""
		self.queue = [num] + self.queue
		return 

	def push_middle(self, num):
		"""push to middle of que"""

		#to get middle
		k = len(self.queue)
		mid = (k+1)//2

		self.queue = self.queue[:mid] +	 [num] + self.queue[mid:]
		
		return

	def get(self, id):
		"""get the element at index id"""
		return self.queue[id]


teque = Teque()
for i in range(int(stdin.readline())):
	inp = stdin.readline().split()


	if inp[0] == 'push_back':
		teque.push_back(int(inp[1]))

	elif inp[0] == 'push_front':
		teque.push_front(int(inp[1]))

	elif inp[0] == 'push_middle':
		teque.push_middle(int(inp[1]))

	elif inp[0] == 'get':
		print(teque.get(int(inp[1])))




# teque = Teque()

# operations = int(input())

# for i in range(operations):
# 	inp = input().split()
# 	operation = inp[0]
# 	num = int(inp[1])

# 	if operation == 'push_back':
# 		teque.push_back(num)

# 	elif operation == 'push_front':
# 		teque.push_front(num)

# 	elif operation == 'push_middle':
# 		teque.push_middle(num)

# 	elif operation == 'get':
# 		print(teque.get(num))

	
	





