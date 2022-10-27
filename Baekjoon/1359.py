# 문제
# 어제, 지민이는 몰래 리조트에 갔다가 입구에 걸려있는 복권 광고를 하나 보았다.

# “1부터 N까지의 수 중에 서로 다른 M개의 수를 골라보세요. 저희도 1부터 N까지의 수 중에 서로 다른 M개의 수를 고를건데, 적어도 K개의 수가 같으면 당첨입니다.!”

# 지민이는 돌아오면서 자신이 복권에 당첨될 확률이 궁금해졌다.

# 지민이가 복권에 당첨될 확률을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 세 정수 N, M, K가 주어진다.

# 출력
# 첫째 줄에 지민이가 복권에 당첨될 확률을 출력한다. 절대/상대 오차는 10-9까지 허용한다.
from math import factorial

n,m,k = map(int,input().split())

def comb(num,chk):
    if num < chk:
        return 0
    else:
        return factorial(num) / (factorial(num-chk) * factorial(chk))

def pos(num,chk,cnt):
    return comb(chk,cnt) * comb(num-chk,chk-cnt) / comb(num, chk)

c = 0
for i in range(k,m+1):
    c += pos(n,m,i)
print(c)