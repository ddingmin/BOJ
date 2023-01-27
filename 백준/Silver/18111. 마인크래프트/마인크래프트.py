n, m, b = map(int, input().split())
maps = []
max_height = 0
min_height = float('inf')

for i in range(n):
    maps.append(list(map(int, input().split())))

ans = []

for h in range(0, 257):
    blocks = b
    time = 0
    for i in maps:
        for j in i:
            if j > h:
                blocks += j - h
                time += 2 * (j - h)
            elif j < h:
                blocks -= h - j
                time += (h - j)
    if blocks >= 0:
        ans.append([time, h])

ans = sorted(ans, key = lambda x: [x[0], -x[1]])
print(*ans[0])
