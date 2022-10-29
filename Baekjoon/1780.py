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

# 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1