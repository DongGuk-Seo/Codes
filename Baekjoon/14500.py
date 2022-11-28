# 문제
# 폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.

# 정사각형은 서로 겹치면 안 된다.
# 도형은 모두 연결되어 있어야 한다.
# 정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
# 정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.



# 아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.

# 테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.

# 테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.

# 입력
# 첫째 줄에 종이의 세로 크기 N과 가로 크기 M이 주어진다. (4 ≤ N, M ≤ 500)

# 둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다. i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수이다. 입력으로 주어지는 수는 1,000을 넘지 않는 자연수이다.

# 출력
# 첫째 줄에 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다.

import sys
input = sys.stdin.readline
n,m = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(n)]
def square():
    score = 0
    for x in range(n-1):
        for y in range(m-1):
            tem = sum([array[x][y],array[x][y+1],array[x+1][y],array[x+1][y+1]])
            if tem > score:
                score = tem
    return score
def bar():
    score = 0
    # 수직
    for x in range(n-3):
        for y in range(m):
            tem = sum([array[x][y],array[x+1][y],array[x+2][y],array[x+3][y]])
            if tem > score:
                score = tem
    # 수평
    for x in range(n):
        for y in range(m-3):
            tem = sum([array[x][y],array[x][y+1],array[x][y+2],array[x][y+3]])
            if tem > score:
                score = tem
    return score
def vertical():
    score = 0
    # 수직
    for x in range(n-2):
        for y in range(m-1):
            xy = array[x][y]
            xy_1 = array[x][y+1]
            x_1y = array[x+1][y]
            x_1y_1 = array[x+1][y+1]
            x_2y = array[x+2][y]
            x_2y_1 = array[x+2][y+1]
            tem_1 = sum([xy,x_1y,x_2y,x_2y_1])
            tem_2 = sum([x_2y,xy_1,x_1y_1,x_2y_1])
            tem_3 = sum([xy,x_1y,x_2y,xy_1])
            tem_4 = sum([xy,xy_1,x_1y_1,x_2y_1])
            tem_5 = sum([xy,x_1y,x_1y_1,x_2y_1])
            tem_6 = sum([xy_1,x_1y,x_1y_1,x_2y])
            tem_7 = sum([xy,x_1y,x_2y,x_1y_1])
            tem_8 = sum([x_1y,xy_1,x_1y_1,x_2y_1])
            high = max(tem_1,tem_2,tem_3,tem_4,tem_5,tem_6,tem_7,tem_8)
            if  high > score:
                score = high
    return score
def horizon():
    score = 0
    # 수평
    for x in range(n-1):
        for y in range(m-2):
            xy = array[x][y]
            x_1y = array[x+1][y]
            x_1y_1 = array[x+1][y+1]
            xy_1 = array[x][y+1]
            xy_2 = array[x][y+2]
            x_1y_2 = array[x+1][y+2]
            tem_1 = sum([xy,xy_1,xy_2,x_1y])
            tem_2 = sum([xy,xy_1,xy_2,x_1y_2])
            tem_3 = sum([x_1y,x_1y_1,x_1y_2,xy_2])
            tem_4 = sum([x_1y,x_1y_1,x_1y_2,xy])
            tem_5 = sum([x_1y,x_1y_1,xy_1,xy_2])
            tem_6 = sum([xy,xy_1,x_1y_1,x_1y_2])
            tem_7 = sum([xy,xy_1,xy_2,x_1y_1])
            tem_8 = sum([x_1y,x_1y_1,x_1y_2,xy_1])
            high = max(tem_1,tem_2,tem_3,tem_4,tem_5,tem_6,tem_7,tem_8)
            if  high > score:
                score = high
    return score
print(max(square(),bar(),vertical(),horizon()))