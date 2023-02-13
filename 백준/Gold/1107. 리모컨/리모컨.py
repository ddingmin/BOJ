from collections import deque
# 풀이
# 1. bfs로 0 <= next_channel < 1_000_001 범위 내 존재하는 누를 수 있는 숫자 버튼 구하기
# 해당 수부터 거리 계산

def push_number_bttn(k, cur_channel, bttns):
    # 숫자 버튼
    return int(cur_channel + str(bttns[k]))

def solve(target_channel, n, bttns):
    visit = [0] * 1_000_001
    q = deque()
    q.append("")
    answer = abs(target_channel - 100)

    count = 1
    while q:
        for _ in range(len(q)):
            cur_channel = q.popleft()
            for k in range(len(bttns)):
                next_channel = int(push_number_bttn(k, cur_channel, bttns))
                if not(0 <= next_channel < 1_000_001): continue
                if visit[next_channel] == 0:
                    visit[next_channel] = 1
                    q.append(str(next_channel))
                answer = min(answer, abs(next_channel - target_channel) + count)

        count += 1
    return answer

channel = int(input())
n = int(input())
bttns = []
if n:
    broken_bttns = list(map(int, input().split()))
    for i in range(10):
        if i in broken_bttns: continue
        bttns.append(i)
else:
    for i in range(10):
        bttns.append(i)
print(solve(channel, n, bttns))