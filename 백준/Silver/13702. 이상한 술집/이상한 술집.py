from collections import deque
input = __import__('sys').stdin.readline

# Input
n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

s, e = 1, max(arr)
res = 0
while s <= e:
    mid = (s + e) // 2
    temp = 0
    for i in arr:
        temp += i // mid
    if temp >= k:
        res = mid
        s = mid + 1
    else:
        e = mid - 1
print(res)