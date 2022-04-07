########
#link https://open.kattis.com/problems/guessthedatastructure
########



def is_stack(inp, out):
	out.reverse()
	
	if inp == out:
		return 1
	else:
		return 0



def is_queue(inp, out):
	if inp == out:
		return 1
	else:
		return 0


def is_priority_queue():
	return










def main():
	n = int(input())

	inp = []
	out = []
	for i in range(n):
		operation, num = list(map(int, input().split()))

		if operation == 1:
			inp.append(num)
		else:
			out.append(num)

	print(inp)
	print(out)

	out.reverse()
	print(out)
	#print(is_queue(inp, out))



if __name__ == "__main__":
	main()