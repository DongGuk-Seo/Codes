# N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다. 우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.

# 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
# 이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 37, N은 3k 꼴)이 주어진다. 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.

# 출력
# 첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.

import sys
input = sys.stdin.readline

n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]

def check (matrix):
    st = 2
    for line in matrix:
        tem = list(set(line))
        if len(tem) > 1:
            return 'Not'
        elif len(tem) == 1 and st == 2:
            st = tem[0]
        else:
            if tem[0] == st:
                pass
            else:
                return 'Not'
    return st

def sep(matrix):
    sep_matrix = []
    if len(matrix[0]) == 3:
        tem = []
        for i in matrix:
            tem += i
        return tem
    else:
        for i in range(3):
            tem = [[],[],[]]
            for line in matrix[(len(matrix)//3)*i:(len(matrix)//3)*(i+1)]:
                for y in range(3):
                    tem[y] += [line[(len(matrix)//3)*y:(len(matrix)//3)*(y+1)]]
            sep_matrix += tem
        return sep_matrix

answer = []

def do(matrix):
    chk = check(matrix)
    if chk == 'Not':
        tem = sep(matrix)
        if type(tem[0]) == int:
            for i in tem:
                answer.append(i)
        else:
            for i in tem:
                answer.append(do(i))
            return
    else:
        return chk

answer.append(do(l))

if n == 1:
    answer = l[0]
m = answer.count(-1)
p = answer.count(1)
z = answer.count(0)
print(m)
print(z)
print(p)