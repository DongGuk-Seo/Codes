# 문제
# 창영이는 4와 7로 이루어진 수를 좋아한다. 창영이가 좋아하는 수 중에 K번째 작은 수를 구해 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 K(1 ≤ K ≤ 109)가 주어진다.

# 출력
# 첫째 줄에 창영이가 좋아하는 숫자 중 K번째 작은 수를 출력한다.

n = int(input())
l = [True,False]
c = 2
t = ''
temp = [True,False]
if n == 1:
    print(4)
elif n == 2:
    print(7)
else:
    while True:
        tem = []
        for x in temp:
            for i in l:
                tem.append(x+i)
                c += 1
                if c == n:
                    break
            if c == n:
                break
        if c == n:
            temp = tem
    print(tem[-1])

4 
7
44
47
74
77
444
447
474
477
744
747
774
777
4444
4447
4474
4477
4744
4747
4774
4777
7444
7447
7474
7477
7744
7747
7774
7777