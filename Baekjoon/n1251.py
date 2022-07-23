# 문제
# 알파벳 소문자로 이루어진 단어를 가지고 아래와 같은 과정을 해 보려고 한다.

# 먼저 단어에서 임의의 두 부분을 골라서 단어를 쪼갠다. 즉, 주어진 단어를 세 개의 더 작은 단어로 나누는 것이다. 각각은 적어도 길이가 1 이상인 단어여야 한다. 이제 이렇게 나눈 세 개의 작은 단어들을 앞뒤를 뒤집고, 이를 다시 원래의 순서대로 합친다.

# 예를 들어,

# 단어 : arrested
# 세 단어로 나누기 : ar / rest / ed
# 각각 뒤집기 : ra / tser / de
# 합치기 : ratserde
# 단어가 주어지면, 이렇게 만들 수 있는 단어 중에서 사전순으로 가장 앞서는 단어를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 영어 소문자로 된 단어가 주어진다. 길이는 3 이상 50 이하이다.

# 출력
# 첫째 줄에 구하고자 하는 단어를 출력하면 된다.

w = input()
wl = [ord(i) for i in w]
point = wl.index(min(wl[:-2]))+1
p1 = wl[:point]
p2 = wl[point:wl[point:-1].index(min(wl[point:-1]))+len(p1)+1]
p3 = wl[wl[point:-1].index(min(wl[point:-1]))+len(p1)+1:]
ans = ''
if p1[-1] < p1[0]:
    for a in p1[::-1]:
        ans += chr(a)
else:
    for a in p1:
        ans += chr(a)
if p2[-1] < p2[0]:
    for b in p2[::-1]:
        ans += chr(b)
else:
    for b in p2:
        ans += chr(b)
if p3[-1] < p3[0]:
    for c in p3[::-1]:
        ans += chr(c)
else:
    for c in p3:
        ans += chr(c)
print(ans)