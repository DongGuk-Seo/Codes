n = int(input())
c = 4
for i in range(int(n**0.5),int((n//4)**0.5),-1):
    if i*i == n:
        c = 1
        break
    else:
        x = n - i*i
        for o in range(int(x**0.5),int((x//3)**0.5),-1):
            if o*o == x:
                c = 2
                break
            else:
                y = n - i*i - o*o
                for p in range(int(y**0.5),int((y//2)**0.5),-1):
                    if p*p == y:
                        c = 3
                        break
print(c)