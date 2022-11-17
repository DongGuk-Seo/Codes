# 문제
# 홀수인 자연수 N이 주어지면, 다음과 같이 1부터 N2까지의 자연수를 달팽이 모양으로 N×N의 표에 채울 수 있다.

# 9	2	3
# 8	1	4
# 7	6	5
# 25	10	11	12	13
# 24	9	2	3	14
# 23	8	1	4	15
# 22	7	6	5	16
# 21	20	19	18	17
# N이 주어졌을 때, 이러한 표를 출력하는 프로그램을 작성하시오. 또한 N2 이하의 자연수가 하나 주어졌을 때, 그 좌표도 함께 출력하시오. 예를 들어 N=5인 경우 6의 좌표는 (4,3)이다.

# 입력
# 첫째 줄에 홀수인 자연수 N(3 ≤ N ≤ 999)이 주어진다. 둘째 줄에는 위치를 찾고자 하는 N2 이하의 자연수가 하나 주어진다.

# 출력
# N개의 줄에 걸쳐 표를 출력한다. 각 줄에 N개의 자연수를 한 칸씩 띄어서 출력하면 되며, 자릿수를 맞출 필요가 없다. N+1번째 줄에는 입력받은 자연수의 좌표를 나타내는 두 정수를 한 칸 띄어서 출력한다.

n = int(input())
target = int(input())
array = [[0 for i in range(n)] for i in range(n)]
ans = []
pos = [n//2,n//2]
array[pos[0]][pos[1]] = 1
if target == 1:
    ans.append([pos[0]+1,pos[1]+1])

def circle(start,point,target):
    startpoint = array[start[0]][start[1]]
    start = [start[0]-1,start[1]]
    for a in range(point):
        startpoint += 1
        array[start[0]][start[1]+a] = startpoint
        if startpoint == target:
            ans.append([start[0]+1,start[1]+a+1])
    start[1] = start[1] + a

    for b in range(1,point+1):
        startpoint += 1
        array[start[0]+b][start[1]] = startpoint
        if startpoint == target:
            ans.append([start[0]+b+1,start[1]+1])
    start[0] = start[0] + b

    for c in range(1,point+1):
        startpoint += 1
        array[start[0]][start[1]-c] = startpoint
        if startpoint == target:
            ans.append([start[0]+1,start[1]-c+1])
    start[1] = start[1] - c

    for d in range(1,point+1):
        startpoint += 1
        array[start[0]-d][start[1]] = startpoint
        if startpoint == target:
            ans.append([start[0]-d+1,start[1]+1])
    start[0] = start[0] - d
    return start

for i in range(1,(n//2)+1):
    if i == 1:
        tem = circle(pos,2,target)
    else:
        tem = circle(tem,2*i,target)

for list in array:
    print(*list)
print(*ans[0])