import sys

input = sys.stdin.readline
n = int(input())
comp = int(input())
l = [[] for i in range(101)]
for i in range(comp):
    cms = list(map(int,input().split()))
    l[cms[0]].append(cms[1])
cnt = 0
for x in l:
    if 1 in x:
        cnt += 1
print(l)
