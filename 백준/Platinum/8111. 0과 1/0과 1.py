import sys
from collections import deque


def solve(target):
    visit = {}
    visit[1] = 1
    q = deque()
    q.append(1)

    while q:
        cur = q.popleft()
        if cur % target == 0:
            return cur

        nxt = cur * 10
        if nxt % target not in visit and len(str(nxt)) < 101:
            visit[nxt % target] = 1
            q.append(nxt)

        nxt2 = cur * 10 + 1
        if nxt2 % target not in visit and len(str(nxt2)) < 101:
            visit[nxt2 % target] = 1
            q.append(nxt2)

    return "BRAK"


def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        print(solve(int(input())))


if __name__ == '__main__':
    main()
