import sys
from collections import deque
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


# dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
# dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

# solve
def solve(cur: int, back: deque, forw: deque, cmd: list):
    if cmd[0] == 'B':
        # 뒤로가기 페이지가 존재한다면.
        if back:
            forw.appendleft(cur)
            cur = back.pop()
    elif cmd[0] == 'F':
        if forw:
            back.append(cur)
            cur = forw.popleft()
    elif cmd[0] == 'A':
        forw.clear()
        if cur is not None:
            back.append(cur)
        cur = int(cmd[1])
    elif cmd[0] == 'C':
        if back:
            new = deque()
            new.append(back.popleft())

            while back:
                if new[-1] == back[0]:
                    back.popleft()
                else:
                    new.append(back.popleft())
            back = new
    # print(f'forward: {forw}, backward: {backward}')
    return cur, back, forw


def out(cur, back, forw):
    print(cur)
    if back:
        print(*list(back)[::-1])
    else:
        print(-1)
    if forw:
        print(*forw)
    else:
        print(-1)


# input
n, q = map(int, input().split())
cur, backward, forward = None, deque(), deque()
for _ in range(q):
    cmd = list(input().split())
    cur, backward, forward = solve(cur, backward, forward, cmd)
out(cur, backward, forward)
