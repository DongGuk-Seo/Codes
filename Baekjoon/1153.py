# 문제
# 임의의 자연수가 주어지면, 이를 네 개의 소수의 합으로 분해하는 프로그램을 작성하시오. 예를 들어 38 = 5 + 7 + 13 + 13이 된다.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

# 출력
# 첫째 줄에 네 개의 소수를 빈 칸을 사이에 두고 순서대로 출력한다. 불가능한 경우는 -1을 출력한다.

n = int(input())

l = [0 for i in range(n+1)]
for i in range(2,1000):
    for x in range(i*2,n+1,i):
        l[x] = 1
p = [i for i in range(2,n+1) if l[i] == 0]
chk = False
if n < 8:
    print(-1)
elif n % 2 == 0:
    n -= 4
    for i in p[::-1]:
        for o in p:
            if i+o == n:
                print(2,2,i,o)
                chk = True
                break
        if chk == True:
            break
else:
    n -= 5
    for i in p[::-1]:
        for o in p:
            if i+o == n:
                print(2,3,i,o)
                chk = True
                break
        if chk == True:
            break

# 골드바흐의 추축을 참으로 가정을 해야 문제를 풀 수 있음