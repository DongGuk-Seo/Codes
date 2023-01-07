sentence = []
while True:
    try:
        sentence += input().split()
    except:
        break
alphabet = {}
for word in sentence:
    for alpha in word:
        try:
            alphabet[alpha] += 1
        except KeyError:
            alphabet[alpha] = 1
max_time = max(alphabet.values())
for i in range(97,123):
    try:
        if alphabet[chr(i)] == max_time:
            print(chr(i),end='')
    except KeyError:
        continue