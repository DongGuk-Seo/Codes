# 문제
# Given a sentence in English, output the counts of consonants and vowels.

# Vowels are letters in [’A’,’E’,’I’,’O’,’U’,’a’,’e’,’i’,’o’,’u’].

# 입력
# The test file starts with an integer S(1 ≤ S ≤ 100), the number of sentences.

# Then follow S lines, each containing a sentence - words of length 1 to 20 separated by spaces. Every sentence will contain at least one word and be comprised only of characters [a-z][A-Z] and spaces. No sentence will be longer than 1000 characters.

# 출력
# For each sentence, output the number of consonants and vowels on a line, separated by space.

n = int(input())
for i in range(n):
    x = list(input().split())
    x = [i.lower() for i in x]
    m = ['a','e','i','o','u']
    nm = 0
    mm = 0
    for i in x:
        for o in i:
            if o not in m:
                nm += 1
            else:
                mm += 1
    print(nm,mm)