from collections import deque

n, k = map(int, input().split())
arr = deque()
for i in range(1, n + 1):
    arr.append(i)

ans = []
while arr:
    for i in range(k - 1):
        arr.append(arr.popleft())
    ans.append(arr.popleft())

print("<" + ", ".join(map(str, ans)) + ">")