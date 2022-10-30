# 문제
# N×M크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다. 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오. 이때, 정사각형은 행 또는 열에 평행해야 한다.

# 입력
# 첫째 줄에 N과 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 수가 주어진다.

# 출력
# 첫째 줄에 정답 정사각형의 크기를 출력한다.

n, m = map(int,input().split())
mat = [list(map(int,list(input()))) for _ in range(n)]
max_num = 0

def check (matrix, x_len, y_len, chk_size):
    max_num = 0
    for x in range(x_len-chk_size):
        for y in range(y_len-chk_size):
            chk_list = [matrix[x][y], matrix[x+chk_size][y], matrix[x][y+chk_size], matrix[x+chk_size][y+chk_size]]
            if chk_list.count(chk_list[0]) == 4:
                max_num = chk_size
            else:
                pass
    return max_num

for i in range(1,n+1):
    tem = check(mat,n,m,i)
    if max_num < tem:
        max_num = tem

print((max_num+1)**2)