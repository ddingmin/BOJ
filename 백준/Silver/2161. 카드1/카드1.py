import sys
from collections import deque


input = sys.stdin.readline
######################### solve ###############################


def solve():
    n = int(input())
    q = deque()
    for i in range(1, n + 1):
        q.appendleft(i)
    answer = []

    while q:
        answer.append(q.pop())
        if q:
            q.appendleft(q.pop())
    print(*answer)


###############################################################

solve()
