import sys
from math import ceil, log2
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

# func
def init(l, r, tree, node = 1):
    if l == r:
        tree[node] = [arr[l], l]
        return
    mid = (l + r) // 2
    init(l, mid, tree, node * 2)
    init(mid + 1, r, tree, node * 2 + 1)
    tree[node] = sorted([tree[node * 2], tree[node * 2 + 1]])[0]
    
def find(LEFT, RIGHT, l, r, tree, node = 1):
    if r < LEFT or RIGHT < l:
        return [float('inf'), float('inf')]
    if LEFT <= l and r <= RIGHT:
        return tree[node]
    mid = (l + r) // 2
    lnode = find(LEFT, RIGHT, l, mid, tree, node * 2)
    rnode = find(LEFT, RIGHT, mid + 1, r, tree, node * 2 + 1)
    return sorted([lnode, rnode])[0]

def solve(l, r, tree):
    h, mid = find(l, r, 0, len(arr) - 1, tree)
    mid_value = h * (r - l + 1)
    left_value, right_value = 0, 0
    if (l <= mid - 1):
        left_value = solve(l, mid - 1, tree)
    if (mid + 1 <= r):
        right_value = solve(mid + 1, r, tree)
    return max(mid_value, left_value, right_value)
# solve
while 1:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    arr = arr[1:]
    H = 2 ** ceil(log2(len(arr)) + 1)
    tree = [0] * H
    init(0, len(arr) - 1, tree)
    print(solve(0, len(arr) - 1, tree))
    