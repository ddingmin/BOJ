input = __import__('sys').stdin.readline

score = list(map(int, input().split()))
n = int(input())
team = [0] * n
for i in range(n):
    for _ in range(3):
        a, b, c = map(int, input().split())
        team[i] += a * score[0]
        team[i] += b * score[1]
        team[i] += c * score[2]

print(max(team))