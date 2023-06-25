import sys
from collections import deque
input = sys.stdin.readline

# 부품수, 적재량, 거리
n, m, t = map(int, input().split())
wait_a, wait_b = deque(), deque()
# 위치, 무게, 준비 시간
for i in range(n):
    a, b, c = map(int, input().split())
    if a == 0:
        # 위치, 무게, 준비시간, i번째 부품, 
        wait_a.append([a, b, c, i + 1])
    else:
        wait_b.append([a, b, c, i + 1])

readyA, readyB = deque(), deque()

answer = [[None, None] for _ in range(n + 1)]

# 위치, 남은 적재량, 다 실었는지
truck = [0, m]
# 초기 시간 설정
if wait_a and wait_b:
    time = min(wait_a[0][2], wait_b[0][2])
elif wait_a:
    time = wait_a[0][2]
elif wait_b:
    time = wait_b[0][2]

while wait_a or wait_b or readyA or readyB:
    # 시간 세팅
    if not (readyA or readyB):
        if wait_a and wait_b:
            time = max(time, min(wait_b[0][2], wait_a[0][2]))
        elif not wait_a and truck[0] == 0:
            time += t
            truck[0] ^= 1
            continue
        elif not wait_b and truck[0] == 1:
            time += t
            truck[0] ^= 1
            continue
        elif wait_b:
            time = max(time, wait_b[0][2])
        elif wait_a:
            time = max(time, wait_a[0][2])
    
    # ready 세팅
    while wait_a and wait_a[0][2] <= time:
        readyA.append(wait_a.popleft())
    while wait_b and wait_b[0][2] <= time:
        readyB.append(wait_b.popleft())
    
    # 실을 수 있다면
    if truck[0] == 0 and readyA:
        while truck[1] > 0 and readyA:
            cur = readyA.popleft()
            if answer[cur[3]][0] == None: answer[cur[3]][0] = time
            if truck[1] >= cur[1]:
                answer[cur[3]][1] = time + t
                truck[1] -= cur[1]
            else:
                cur[1] -= truck[1]
                truck[1] = 0
                readyA.appendleft(cur)

    if truck[0] == 1 and readyB:
        while truck[1] > 0 and readyB:
            cur = readyB.popleft()
            if answer[cur[3]][0] == None: answer[cur[3]][0] = time
            if truck[1] >= cur[1]:
                answer[cur[3]][1] = time + t
                truck[1] -= cur[1]
            else:
                cur[1] -= truck[1]
                truck[1] = 0
                readyB.appendleft(cur)
    
    time += t
    truck[0] ^= 1
    truck[1] = m


for i in range(1, len(answer)):
    print(*answer[i])