# 문제
# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

# 입력
# 첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

# 출력
# 첫째 줄에 자연수 N의 최댓값을 출력한다.

n = int(input())
c = 0
t = 0
for i in range(1,n):
    if c >= n:
        break
    else:
        c += i
        t += 1
if c > n:
    print(t-1)
elif n == 1:
    print(1)
else:
    print(t)