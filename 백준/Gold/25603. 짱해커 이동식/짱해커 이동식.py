from collections import deque
input = __import__('sys').stdin.readline

n, k = map(int, input().split())
cost = list(map(int, input().split()))

def solve():
    s = 0
    minCost = cost[0]
    ans = cost[0]
    # 첫 의뢰 수락
    for i in range(s, s + k):
        if cost[i] <= minCost:
            minIdx = i
            minCost = cost[i]
            ans = minCost
    s = minIdx + 1
    
    while s + k <= n:
        q = deque()
        i = s
        minWindow = 0
        # 윈도우 만들기
        for j in range(i, n):
            # 슬라이딩 윈도우가 k개가 되기 전에 최소 비용중 최댓값(구하려는 답)보다 작은 값이 발견한 경우
            if cost[j] <= ans:
                # 슬라이딩 윈도우를 현재 idx의 다음부터 다시 탐색
                s = j + 1
                break
            
            else:
                # 큐에 값을 현재 넣음
                q.append(cost[j])
                # 슬라이딩 윈도우 중에 가장 작은 값, 해당 인덱스 초기 세팅
                if minWindow == 0: 
                    minWindow = cost[j]
                    minWindowIdx = j
                else:
                    # 윈도우 내에 최소 값, 인덱스 갱신
                    if cost[j] <= minWindow:
                        minWindow = cost[j]
                        minWindowIdx = j
                
                # 만약 윈도우가 다 찼다면 답 갱신
                if len(q) >= k:
                    s = minWindowIdx + 1
                    ans = minWindow
                    break
    return ans
print(solve())
