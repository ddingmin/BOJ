import sys
input = sys.stdin.readline

MAX_SCORE = [100, 100, 200, 200, 300, 300, 400, 400, 500]

scores = list(map(int, input().split()))

answer = "none"
count = 0
for i in range(len(MAX_SCORE)):
    if scores[i] > MAX_SCORE[i]:
        print("hacker")
        exit(0)
    else:
        count += scores[i]

if count >= 100:
    answer = "draw"
print(answer)