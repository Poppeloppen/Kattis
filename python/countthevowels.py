########
#link https://open.kattis.com/problems/countthevowels
########

vowel_dict = {'a': 1,
            'e': 1,
            'i': 1,
            'o': 1,
            'u': 1}

inp =input().lower()

vowel_cnt = 0
for i in inp:
    if i in vowel_dict:
        vowel_cnt += 1

print(vowel_cnt)
