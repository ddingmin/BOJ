import sys
from collections import deque

input = sys.stdin.readline

# input
n, k = map(int, input().split())

q = deque()

for i in range(1, n + 1):
    q.append(i)

while len(q) > k:
    q.append(q.popleft())
    for _ in range(k - 1):
        q.popleft()

print(q[0])
