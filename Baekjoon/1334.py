n = input()
if len(n) % 2 == 1:
    n = str(int(n) + 1)
    f = int(n[:len(n)//2])
    b = int(n[len(n)//2:])
    while str(f) != str(b)[1:][::-1]:
        b += 1
    print(str(f)+str(b))
elif len(n) == 1:
    print(int(n)+1)
else:
    n = str(int(n) + 1)
    f = int(n[:len(n)//2])
    b = int(n[len(n)//2:])
    while True:
        if len(str(b)) % 2 == 0:
            if str(f) != str(b)[::-1]:
                break
        else:
            if str(f) != str(b)[1:][::-1]:
                break
        b += 1 
        print(str(f)+str(b))
        