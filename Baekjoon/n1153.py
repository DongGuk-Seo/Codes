pl = []
x = 10000
for i in range(2,x):
    c = 0
    for o in range(2,i):
        if i%o == 0:
            c += 1
    if c == 1:
        pl.append(i)
print(pl)