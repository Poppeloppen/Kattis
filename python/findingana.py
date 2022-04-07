########
#link https://open.kattis.com/problems/findingana
########

inp = input()

t = [l for l in inp]

a_idx = 0
for i, letter in enumerate(t):
    if letter == 'a':
        a_idx = i
        break

letters = t[a_idx:]
print(''.join(letters))
