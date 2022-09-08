import heapq
input = __import__('sys').stdin.readline

# 중앙값 보다 크면 큰 힙에 넣고, 작으면 작은 힙에 넣기
n = int(input())
big, small = [], []
middle = int(input())
for _ in range(n - 1):
    print(middle)
    ipt = int(input())
    # 큰 힙에서는 가장 작은 값, 작은 힙에서는 가장 큰 값이 중간값으로 갱신
    
    # 입력값이 더 큰 경우
    if ipt > middle: heapq.heappush(big, ipt)
    # 작은 경우
    else: heapq.heappush(small, -1 * ipt)
    
    if 0 <= len(big) - len(small) <= 1: continue
    else:
        # 큰 힙이 더 많을 경우
        # 큰 힙에 존재하는 가장 작은 값을 중간 값으로
        # 기존 중간 값은 작은 힙으로
        if len(big) > len(small):
            heapq.heappush(small, -1 * middle)
            middle = heapq.heappop(big)
        # 작은 힙이 더 많은 경우는 반대로
        else:
            heapq.heappush(big, middle)
            middle = -1 * heapq.heappop(small)
print(middle)