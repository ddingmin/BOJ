import sys
from math import ceil, log2
input = sys.stdin.readline

# init
n, m = map(int, input().split())
H = 2 ** ceil(log2(n) + 1)
arr = [0] * n
tree = [0] * H

# func
def init(l = 0, r = n - 1, node = 1):
    if l == r:
        tree[node] = arr[l]
        return
    mid = (l + r) // 2
    init(l, mid, node * 2)
    init(mid + 1, r, node * 2 + 1)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def update(index, diff, l = 0, r = n - 1, node = 1):
    if not(l <= index <= r):
        return
    tree[node] += diff
    if l == r:
        return
    mid = (l + r) // 2
    update(index, diff, l, mid, node * 2)
    update(index, diff, mid + 1, r, node * 2 + 1)

def find(LEFT, RIGHT, l = 0, r = n - 1, node = 1):
    if r < LEFT or RIGHT < l:
        return 0
    if LEFT <= l and r <= RIGHT:
        return tree[node]
    mid = (l + r) // 2
    lnode = find(LEFT, RIGHT, l, mid, node * 2)
    rnode = find(LEFT, RIGHT, mid + 1, r, node * 2 + 1)
    return lnode + rnode

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b - 1, c)
        arr[b - 1] += c
    elif a == 2:
        print(find(b - 1, c - 1))