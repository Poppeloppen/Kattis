########
#link https://open.kattis.com/problems/joinstrings
########


def preprocess(x):
    return int(x)-1

def unoptimized(n=None, strings_tmp=None):
    #n = int(input())
    
    strings = ['' for i in range(n)]
    
    for i in range(n):
        strings[i] = strings_tmp[i]
    #for i in range(n):
    #    strings[i] = input()
    """
    for i in range(n-1):
        a, b = list(map(preprocess, input().split()))

        strings[a] = strings[a]+strings[b]
        strings[b] = ''

    print(*[x for x in strings if x != ''])
    """
    return strings


def optimized(n=None, strings_tmp=None):
    #n = int(input())

    #This is probaly irrelevant when the next list comprehension is used
    #strings = [''] * n
    
    strings = [i for i in strings_tmp]
    for i in range(n-1):
        a, b = list(map(preprocess, input().split()))

        strings[a] = strings[a]+strings[b]
        strings[b] = ''

    print(*[x for x in strings if x != ''])
    return 





n = int(input())

#This is probaly irrelevant when the next list comprehension is used

strings = [input() for _ in range(n)]
for i in range(n-1):
    a, b = list(map(preprocess, input().split()))

    strings[a] = strings[a]+strings[b]
    strings[b] = ''

print(*[x for x in strings if x != ''])
 



################# optimization #################

##import timeit
#
#if __name__ == "__main__":
#    from sys import stdin
#
#    #### The input from stdin
#    lines = stdin.readlines()
#    n = int(lines[0])
#    strings_tmp = [line.strip() for line in lines[1:n+1]]
#    operations = [list(map(int, line.strip().split())) for line in lines[n+1:] ]
#
#
#    print(n)
#    print(strings_tmp)
#    print(operations)
#    print("UNoptimized")
#    #print(timeit.timeit("unoptimized(n)", "from __main__ import unoptimized, n", number=1))
#    print("optimized")
#    print(timeit.timeit("optimized(n)", "from __main__ import optimized, n, strings_tmp", number=1))
#
#
    #print(timeit.timeit("test(n)", "from __main__ import test, n", number=10))

#### The creation of the empty string
#print('#'*15, 'Making the empty string', '#'*15)
#t2 = timeit.Timer('["" for i in range(40)]')
#print('unoptimized:\t', t2.timeit())
#t = timeit.Timer('strings = [''] * 40') 
#print('optimized:\t', t.timeit())
#print()
#
#### Populating the empty string
#print('#'*15, 'Populating the empty string', '#'*15)
#t3 = timeit.Timer('for i in range(40): string[i] = 1',setup = "string=['']*40")
#print('unoptimized:\t', t3.timeit())
#t4 = timeit.Timer('[1 for i in range(40)]',setup = "string=['']*40")
#print('optimized:\t', t4.timeit())
#print()
#
#
#
#
