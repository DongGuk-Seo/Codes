# 문제
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
m = 0
z = 0
p = 0
c = 1
cc = 0
for i in l:
    for o in i:
        if o == 0:
            z += 1
        elif o == 1:
            p += 1
        else:
            m += 1
else:
    while True:
        c *= 3
        for o in range(n//c):
            for i in range(n//c):
                tem = []
                for x in l[o*c:(o+1)*c]:
                    tem += x[i*c:(i+1)*c]
                if tem.count(1) == c*c:
                    p -= c*c-(c**cc)
                elif tem.count(0) == c*c:
                    z -= c*c-(c**cc)
                elif tem.count(-1) == c*c:
                    m -= c*c-(c**cc)
                else:
                    pass
        cc += 1
        if c == n:
            break
    print(m)
    print(z)
    print(p)