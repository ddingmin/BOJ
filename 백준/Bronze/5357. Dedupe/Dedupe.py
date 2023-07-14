import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    temp = deque(input().strip())
    ans = deque()

    for i in range(len(temp)):
        if not ans:
            ans.append(temp[i])
        elif ans[-1] != temp[i]:
            ans.append(temp[i])
    print("".join(map(str, ans)))