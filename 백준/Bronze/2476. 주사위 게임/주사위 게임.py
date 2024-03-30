n = int(input())

ans = 0

for _ in range(n):
    visit = [0] * 7
    a, b, c = map(int, input().split())

    tmp = 0
    visit[a] += 1
    visit[b] += 1
    visit[c] += 1

    for i in range(1, 7):
        if visit[i] == 3:
            ans = max(ans, 10000 + i * 1000)
            break
        if visit[i] == 2:
            ans = max(ans, 1000 + i * 100)
            break
        ans = max(ans, i * 100)

print(ans)
