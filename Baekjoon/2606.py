import sys

input = sys.stdin.readline
n = int(input())
n_comp = int(input())
l = [[] for i in range(n+1)]
for i in range(n_comp):
    cms = list(map(int,input().split()))
    l[cms[0]].append(cms[1])
    l[cms[1]].append(cms[0])
inf = set()
visit = [[0] for i in range(n+1)]
cnt = 1

def check_fir(n):
    visit[n] = 1
    for x in l[n]:
        inf.add(x)
    return l[n]

def check_oth(n):
    global cnt
    if cnt > 100:
        return
    else:    
        tem = set()
        for x in n:
            if visit[x] == 0:
                continue
            else:
                visit[x] = 1
                for y in l[x]:
                    inf.add(y)
                    tem.add(y)
        cnt+=1 
        return check_oth(list(tem))

check_oth(check_fir(1))
print(len(inf)-1)