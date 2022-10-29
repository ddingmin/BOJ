from collections import deque
input = __import__('sys').stdin.readline

target = int(input())
copyEmo = 0
visit = [[0] * 1001 for _ in range(1001)]

def do(k, emo, cE):
    if k == 0:  # 복사
        return (emo, emo)
    elif k == 1:    # 붙여넣기
        return (emo + cE, cE)
    else:   # 삭제
        return (emo - 1, cE)

def bfs(target):
    q = deque()
    q.append((1, 0, 0))    # emo, copyEmo, cnt
    visit[1][0] = 1
    while q:
        emo, copyEmo, cnt = q.popleft()
        if emo == target:
            return cnt
        for k in range(3):
            e, cE = do(k, emo, copyEmo)
            if cE == 0 and k == 1: continue # 붙여넣을 때 복사된 값이 0인 경우
            if not(0 <= e < 1001): continue
            if visit[e][cE] == 0:
                visit[e][cE] = 1
                q.append((e, cE, cnt + 1))

print(bfs(target))