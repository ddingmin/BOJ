import sys
from math import ceil, log2
input = sys.stdin.readline

# init
n, m = map(int, input().split())
arr = list(map(int, input().split()))
H = 2 ** ceil(log2(n) + 1)
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
    if not (l <= index <= r): return
    if l == r: 
        tree[node] += diff
        return
    mid = (l + r) // 2
    update(index, diff, l, mid, node * 2)
    update(index, diff, mid + 1, r, node * 2 + 1)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def find(LEFT, RIGHT, l = 0, r = n - 1, node = 1):
    if r < LEFT or RIGHT < l:
        return 0
    if LEFT <= l and r <= RIGHT:
        return tree[node]
    
    mid = (l + r) // 2
    return find(LEFT, RIGHT, l, mid, node * 2) + find(LEFT, RIGHT, mid + 1, r, node * 2 + 1)

# solve
init()
for _ in range(m):
    x, y, a, b = map(int, input().split())
    x, y = min(x, y), max(x, y)
    print(find(x - 1, y - 1))
    diff = b - arr[a - 1]
    update(a - 1, diff)
    arr[a - 1] = b