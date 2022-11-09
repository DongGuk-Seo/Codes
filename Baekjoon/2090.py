# 문제
# N개의 수 A[1], …, A[N]의 조화평균은 1/(1/A[1] + 1/A[2] + … + 1/A[N]) 으로 정의된다. 즉, 각각의 수들을 뒤집어서(분모와 분자) 모두 더한 뒤, 그 값을 다시 뒤집는 것이다. 예를 들어 1, 2, 4의 조화평균을 구하면 4/7이 된다.

# N개의 자연수 A[1], …, A[N]이 주어졌을 때, 그 조화평균을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1≤N≤9)이 주어진다. 다음 줄에는 차례로 A[1], …, A[N]이 주어진다. 각 수들은 자연수이며, 100을 넘지 않는다.

# 출력
# 첫째 줄에 분수 형태로 답을 출력한다. 답을 표현하는 방법이 여러 가지 있을 수 있는데, 그 중에서 가장 적은 수의 문자(숫자 및 /)를 사용하는 답을 출력하고, 그러한 경우가 여럿 있다면 사전 식으로 제일 앞서는 것을 출력한다.
import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int,input().split()))
tem = []
top = 0
bottom = 0
def euclidean (a, b):
    r = a % b
    if r == 0:
        return b
    else:
        a = b
        b = r
        return euclidean(a,b)

for num in range(n):
    x = 1
    for c in range(n):
        if num == c:
            pass
        else:
            x *= l[c]
    bottom += x
top = x*l[num]

e = euclidean(top,bottom)
print(f'{top//e}/{bottom//e}')