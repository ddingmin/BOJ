import sys
from collections import deque


def solve(arr):
    pass


def main():
    n, m = map(int, input().split())
    q = deque()
    for i in range(1, n + 1):
        q.append(i)
    ans = 0
    arr = list(map(int, input().split()))

    for target in arr:
        m = 0
        for i in range(len(q)):
            if target == q[i]:
                ans += min(i, len(q) - i)
                m = i

        for _ in range(m):
            q.append(q.popleft())
        q.popleft()

    print(ans)

if __name__ == '__main__':
    input = sys.stdin.readline
    main()
