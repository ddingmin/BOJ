import sys
input = sys.stdin.readline

score = {'D': 0,
         'P': 0}

n = int(input())
for _ in range(n):
    name = input().strip()
    score[name] += 1
    if abs(score['D'] - score['P']) > 1:
        break

print(str(score['D']) + ":" + str(score['P']))
