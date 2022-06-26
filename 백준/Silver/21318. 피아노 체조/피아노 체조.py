from collections import deque
input = __import__('sys').stdin.readline

# Input
n = int(input())
d = list(map(int, input().split()))

# 누적합을 위한 첫번째 index는 0
d = [0] + d
q = int(input())

# 누적합을 담을 배열
fail = [0] * (n + 1)

# 누적합 계산 실패면 1 설정하고 아니면 0 
# 이후 자기 자신의 앞 수를 더해 누적합 배열 생성
for i in range(n): 
    if d[i] > d[i + 1]:
        fail[i] = 1
    if i == 0: continue
    fail[i] += fail[i-1]

# 답 출력
for _ in range(q):
    x, y = map(int, input().split())
    ans = fail[y-1] - fail[x-1]
    print(ans)