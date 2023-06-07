import sys
from math import ceil, log

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

# input
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
H = 2 ** ceil(log(n, 2) + 1)
tree = [0] * H


# func
def init(l=0, r=n - 1, node=1):
    if l == r:
        # 최소높이, 인덱스
        tree[node] = [arr[l], l]
        return

    mid = (l + r) // 2
    init(l, mid, node * 2)
    init(mid + 1, r, node * 2 + 1)
    tree[node] = sorted([tree[node * 2], tree[node * 2 + 1]])[0]


def find(LEFT, RIGHT, l=0, r=n - 1, node=1):
    if r < LEFT or RIGHT < l: return [float('inf'), float('inf')]
    if LEFT <= l and r <= RIGHT:
        return tree[node]
    mid = (l + r) // 2
    return sorted([find(LEFT, RIGHT, l, mid, node * 2),
                  find(LEFT, RIGHT, mid + 1, r, node * 2 + 1)])[0]


def find_ans(l = 0, r = n - 1):
    if l == r:
        return arr[l]

    h, mid = find(l, r)

    lvalue, rvalue = 0, 0
    if l <= mid - 1:
        lvalue = find_ans(l, mid - 1)
    if mid + 1 <= r:
        rvalue = find_ans(mid + 1, r)

    return max(lvalue, rvalue, h * (r - l + 1))
    

# solve
init()
print(find_ans())
