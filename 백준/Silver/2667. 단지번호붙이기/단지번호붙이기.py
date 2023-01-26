from collections import deque

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, list(input()))))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visit = [[0] * n for _ in range(n)]

def count_home(x, y):
    count = 1
    q = deque()
    q.append((x, y))
    visit[x][y] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if not(0 <= x < n and 0 <= y < n): continue
            if arr[x][y] == 1 and visit[x][y] == 0:
                count += 1
                visit[x][y] = 1
                q.append((x, y))
    return count

answer = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visit[i][j] == 0:
            count = count_home(i, j)
            if count:
                answer.append(count)

answer.sort()
print(len(answer))
for a in answer:
    print(a)
    