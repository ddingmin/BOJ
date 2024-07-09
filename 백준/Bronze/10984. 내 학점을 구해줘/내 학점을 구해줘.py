t = int(input())
for i in range(t):
    grade_sum = 0
    score_sum = 0
    n = int(input())
    for j in range(n):
        c, g = map(float, input().split())
        grade_sum += c
        score_sum += g*c
    print("{0:.0f} {1:.1f}".format(grade_sum, score_sum/grade_sum))