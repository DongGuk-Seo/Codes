# 문제
# Little hobbitses go to hobbit school in the Shire. They just finished a course, which involved tea-making, meal-eating, nap-taking, and gardening. Based on the following grading scale, assign each hobbit a letter grade based on their final numerical course grade.

# A+: 97-100
# A: 90-96
# B+: 87-89
# B: 80-86
# C+: 77-79
# C: 70-76
# D+: 67-69
# D: 60-66
# F: 0-59
# 입력
# The input will begin with a single line containing just a whole number, n, of the number of hobbits in the class, followed by n lines in the form a b, where a is the hobbit’s name (only alphabetical characters) and b is the hobbit’s grade, given as a whole number. The length of hobbit's name is less than 10.

# 출력
# For each test case, print out a list of every hobbits name and letter grade, each on its own line. There should be no additional white space following test cases.

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