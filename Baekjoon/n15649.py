# 문제
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 입력
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

# 출력
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

n, m = map(int,input().split())
n_l = [i for i in range(1,n+1)]
chk_l = [False for i in range(n)]

def back(x,num_l,chk_other):
    for i in range(1,x+1):
        
def track(chk, num_l, m):
    for i in num_l:
        l = [i]
        for o in range(m):
            l += back()
        chk[i-1] = True
    print(*l)        