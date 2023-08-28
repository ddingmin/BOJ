from collections import deque

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr = sorted(arr, reverse = 1)

ans = 0
for i in range(2, len(arr), 3):
    ans += arr[i]

print(sum(arr) - ans)