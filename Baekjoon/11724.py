# 문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int,input().split())

l = [[] for i in range(n+1)]
visit = [False for i in range(n+1)]
for i in range(m):
    x, y = map(int,input().split())
    l[x].append(y)
    l[y].append(x)

num = 0
def graph(nodes):
    for node in nodes:
        if visit[node] == True:
            pass
        else:
            visit[node] = True
            graph(l[node])
    return

for i in range(1,n+1):
    if visit[i] == True:
        pass
    else:
        graph(l[i])
        num += 1
print(num)