from collections import deque
input = __import__('sys').stdin.readline

n = int(input())

arr = []
for i_ in range(n):
    t = list(map(int,input().split()))
    arr.append(t)

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

ans = 0
for h in range(0, 101):
    check = [[False] * n for _ in range(n)]
    val = 0
    q = deque()
    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                # 시작 노드
                q.append((i,j))
                check[i][j] = True
                if arr[i][j] > h: # 조건이 참이면
                    val += 1
                    while(q):
                        temp = q.popleft()
                        for d in range(4):
                            dx = temp[0] + dir[d][0]
                            dy = temp[1] + dir[d][1]
                            if 0 <= dx < n and 0 <= dy < n and not check[dx][dy]:
                                check[dx][dy] = True
                                if arr[dx][dy] > h:
                                    q.append((dx,dy))
                else:
                    q.popleft()
    ans = max(val, ans)
print(ans)