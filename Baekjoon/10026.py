# 문제
# 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

# 크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

# 예를 들어, 그림이 아래와 같은 경우에

# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR
# 적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

# 그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

n = int(input())
n_list = []
an_list = []
l = [input() for _ in range(n)]
for i in l:
    n_list.append(list(i))
    an_list.append(list(i.replace('G','R')))
n_visit = [[0 for i in range(n)] for i in range(n)]
an_visit = [[0 for i in range(n)] for i in range(n)]

def spread (area,x,y,vt,chk):
    if vt[x][y] == 1:
        return
    else:
        if area[x][y] == chk:
            vt[x][y] = 1
            for a in range(-1,2,2):
                if x+a >= 0 and x+a <= n-1:
                    spread(area,x+a,y,vt,chk)
            for b in range(-1,2,2):
                if y+b >= 0 and y+b <= n-1:
                    spread(area,x,y+b,vt,chk)
            return
        else:
            return

def check (area, vst, num):
    v = 0
    for x in range(num):
        for y in range(num):
            if vst[x][y] == 0:
                vst[x][y] = 1
                chk = area[x][y]
                for a in range(-1,2,2):
                    if x+a >= 0 and x+a <= num-1:
                        spread(area,x+a,y,vst,chk)
                for b in range(-1,2,2):
                    if y+b >= 0 and y+b <= num-1:
                        spread(area,x,y+b,vst,chk)
                v += 1
            else:
                pass
    return v

print(check(n_list, n_visit, n),check(an_list, an_visit, n))