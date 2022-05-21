def test(x):
    if x <= 59:
        return 'F'
    elif x <= 66:
        return 'D'
    elif x <= 69:
        return 'D+'
    elif x <= 76:
        return 'C'
    elif x <= 79:
        return 'C+'
    elif x <= 86:
        return 'B'
    elif x <= 89:
        return 'B+'
    elif x <= 96:
        return 'A'
    else:
        return 'A+'
n = int(input())
for i in range(n):
    student, score = input().split()
    print(student, test(int(score)))