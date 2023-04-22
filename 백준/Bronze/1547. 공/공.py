m = int(input())
cups = [0] * 4
cups[1] = 1
for _ in range(m):
    a, b = map(int, input().split())
    cups[a], cups[b] = cups[b], cups[a]

for i in range(1, 4):
    if cups[i] == 1:
        print(i)