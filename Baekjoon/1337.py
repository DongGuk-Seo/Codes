# 문제
# 올바른 배열이란 어떤 배열 속에 있는 원소 중 5개가 연속적인 것을 말한다. (연속적인 것이란 5개의 수를 정렬했을 때, 인접한 수의 차이가 1인 것을 말한다.)

# 예를 들어 배열 {6, 1, 9, 5, 7, 15, 8}은 올바른 배열이다. 왜냐하면 이 배열 속의 원소인 5, 6, 7, 8, 9가 연속이기 때문이다.

# 배열이 주어지면, 이 배열이 올바른 배열이 되게 하기 위해서 추가되어야 할 원소의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 배열의 크기 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 배열의 원소가 한 줄에 하나씩 주어진다. 원소는 1,000,000,000보다 작거나 같은 음이 아닌 정수이다. 배열에 중복되는 수는 없다.

# 출력
# 첫째 줄에 입력으로 주어진 배열이 올바른 배열이 되게 하기 위해서 추가되어야할 원소의 최소 개수를 출력한다.

n = int(input())
nums = [int(input()) for _ in range(n)]
dic = {i:[0]*8 for i in nums}
for s_num in nums:
    for m_num in nums:
        if s_num == m_num:
            pass
        else:
            x = m_num - s_num
            if -4 <= x <= 4:
                if x < 0:
                    dic[s_num][x+4] = 1
                else:
                    dic[s_num][x+3] = 1
sum_dic = {i:0 for i in nums}
for num in nums:
    for x in range(5):
        if sum_dic[num] < sum(dic[num][x:x+4]):
            sum_dic[num] = sum(dic[num][x:x+4])

print(4 - max(list(sum_dic.values())))