import heapq
input = __import__('sys').stdin.readline

n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

# 회의 시작시간, 종료시간 순으로 다중 정렬
arr = sorted(arr, key = lambda x: [x[0], x[1]])

# 첫번째 회의 종료시간을 넣기
ans = 1
begin = [] # 종료시간은 회의 가능 시간임.
a, b = arr[0]
heapq.heappush(begin, b)

# 종료시간 보다 시작시간이 크거나 같다면 해당 회의실을 비우고 사용
for k in range(1, n):
    a, b = arr[k]
    if a >= begin[0]:
        heapq.heappop(begin)
    heapq.heappush(begin, b)
    ans = max(ans, len(begin))

print(ans)