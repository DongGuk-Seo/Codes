# 문제
# 홀수 정수 N이 주어지면 1과 N 사이의 모든 홀수 정수의 합을 계산합니다.

# 입력
# 입력의 첫 번째 줄에는 테스트 케이스의 수인 T가 포함됩니다. 각 테스트 케이스는 단일 정수 N을 포함합니다. N은 1에서 100 사이입니다.

# 출력
# 각 테스트 케이스에 대해 1+3+….+N 값을 출력합니다.

import sys
input = sys.stdin.readline
n = int(input())
l = [(2*i+1) for i in range(101)]
for i in range(n):print(sum(l[:l.index(int(input()))+1]))