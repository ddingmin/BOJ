# BOJ 9328

# 열쇠 주으면 visit 초기화, 시작 위치에서 다시 돌리기

from collections import deque

t = int(input())
for ttt in range(t):
    n, m = map(int, input().split())
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우
    arr = []
    startDir = []
    visit = [[0] * m for _ in range(n)]

    for i in range(n):
        temp = list(input())
        for j in range(m):
            if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                if temp[j] == '.' or (ord('a') <= ord(temp[j]) <= ord('z')): startDir.append((i, j))
                if ord('A') <= ord(temp[j]) <= ord('Z'): startDir.append((i, j))
                if temp[j] == '$': startDir.append((i, j))
        arr.append(temp)

    # 열쇠 정보
    key = [0] * 30
    keylist = list(input())
    if keylist[0] != '0':
        for k in keylist:
            key[ord(k) - ord('a')] = 1

    def bfs(visit):
        global ans
        q = deque()
        for i, j in startDir:
            if arr[i][j] == '.':
                q.append((i, j))
                visit[i][j] = 1
            elif ord('a') <= ord(arr[i][j]) <= ord('z'):
                q.append((i, j))
                key[ord(arr[i][j]) - ord('a')] = 1
                arr[i][j] = '.'
                visit[i][j] = 1
            elif ord('A') <= ord(arr[i][j]) <= ord('Z'):
                if key[ord(arr[i][j]) - ord('A')] == 1:
                    arr[i][j] = '.'
                    q.append((i, j))
                    visit[i][j] = 1
            elif arr[i][j] == '$':
                q.append((i, j))
                visit[i][j] = 1
                ans += 1
                arr[i][j] = '.'


        while q:
            i, j = q.popleft()
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if not(0 <= x < n and 0 <= y < m): continue
                if visit[x][y] == 1: continue
                if arr[x][y] == '$':
                    q.append((x, y))
                    visit[x][y] = 1
                    arr[x][y] = '.'
                    ans += 1

                elif arr[x][y] == '.':
                    q.append((x, y))
                    visit[x][y] = 1

                # 열쇠 처리
                elif ord('a') <= ord(arr[x][y]) <= ord('z'):
                    if key[ord(arr[x][y]) - ord('a')] == 1:
                        q.append((x, y))
                        arr[x][y] = '.'
                        visit[x][y] = 1
                    else:
                        q.append((x, y))
                        key[ord(arr[x][y]) - ord('a')] = 1
                        arr[x][y] = '.'
                        q.clear()
                        visit = [[0] * m for _ in range(n)]

                        for i, j in startDir:
                            if arr[i][j] == '.':
                                q.append((i, j))
                                visit[i][j] = 1
                            elif ord('a') <= ord(arr[i][j]) <= ord('z'):
                                q.append((i, j))
                                key[ord(arr[i][j]) - ord('a')] = 1
                                arr[i][j] = '.'
                                visit[i][j] = 1
                            elif ord('A') <= ord(arr[i][j]) <= ord('Z'):
                                if key[ord(arr[i][j]) - ord('A')] == 1:
                                    arr[i][j] = '.'
                                    q.append((i, j))
                                    visit[i][j] = 1


                elif ord('A') <= ord(arr[x][y]) <= ord('Z'):
                    if key[ord(arr[x][y]) - ord('A')] == 1:
                        arr[x][y] = '.'
                        q.append((x, y))
                        visit[x][y] = 1


    ans = 0
    bfs(visit)
    print(ans)

    # for k in arr:
    #     print(*k)
