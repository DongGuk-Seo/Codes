l = []
for i in range(1,int(50000**0.5)+1):
    l.append(i**2)
n = int(input())
c = 4
for i in range(int(n**0.5),0,-1):
    x = n - l[i-1]
    if x == 0:
        c = 1
        break
    else:
        for o in range(int(x**0.5),0,-1):
            y = x - l[o-1]
            if y == 0:
                c = 2
                break
            else:
                for p in range(int(y**0.5),0,-1):
                    z = y - l[p-1]
                    print(x,y,z)
                    if z == 0:
                        c = 3
                        break
print(c)