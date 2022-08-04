from collections import deque
input = __import__('sys').stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 원생들의 키 차이를 나타내는 배열
cost = []
for i in range(1, len(arr)):
    cost.append(arr[i] - arr[i - 1])
    
# 한 조를 줄일 때 마다 가장 최소 비용을 더해주면 됨. 즉 n - k만큼 더하면 k조가 되는 최소 비용
cost.sort()
ans = 0
for i in range(n - k):
    c = cost[i]
    ans += c
print(ans)