import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    worm = 0
    w,h,k = map(int,input().split())
    land = [[0 for i in range(w)] for i in range(h)]
    for i in range(k):
        a,b = map(int,input().split())
        land[b][a] = 1
    
    def check(l,curr_b,curr_a):
        global c
        if l[curr_b][curr_a] == 1:
            l[curr_b][curr_a] = 0
            c = False

        if curr_b == 0:
            for y in range(1,2):
                try:
                    if l[curr_b+y][curr_a] == 1:
                        l[curr_b+y][curr_a] = 0
                        check(l,curr_b+y,curr_a)
                        c = False
                except:
                    pass
        else:
            for y in range(-1,2,2):
                try:
                    if l[curr_b+y][curr_a] == 1:
                        l[curr_b+y][curr_a] = 0
                        check(l,curr_b+y,curr_a)
                        c = False
                except:
                    pass
        if curr_a == 0:
            for x in range(1,2):
                try:
                    if l[curr_b][curr_a+x] == 1:
                        l[curr_b][curr_a+x] = 0
                        check(l,curr_b,curr_a+x)
                        c = False
                except:
                    pass
        else:
            for x in range(-1,2,2):
                try:
                    if l[curr_b][curr_a+x] == 1:
                        l[curr_b][curr_a+x] = 0
                        check(l,curr_b,curr_a+x)
                        c = False
                except:
                    pass
        return l

    for b in range(h):
        for a in range(w):
            c = True
            land[b][a] == 1
            check(land,b,a)
            if c == False:
                worm += 1
    print(worm)