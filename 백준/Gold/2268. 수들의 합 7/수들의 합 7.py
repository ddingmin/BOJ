import sys
import math
input = sys.stdin.readline

# init
n, m = map(int, input().split())
arr = [0] * n
H = 2 ** math.ceil(math.log2(n) + 1)
tree = [0] * H

# code
def init(l = 0, r = n - 1, node = 1):
    if l == r:
        tree[node] = arr[l]
        return
    mid = (l + r) // 2
    init(l, mid, node * 2)
    init(mid + 1, r, node * 2 + 1)

def modify(index, diff, l = 0, r = n - 1, node = 1):
    if not(l <= index <= r): return 
    tree[node] += diff
    if l == r: return
    mid = (l + r) // 2
    modify(index, diff, l, mid, node * 2)
    modify(index, diff, mid + 1, r, node * 2 + 1)

def find(LEFT, RIGHT, l = 0, r = n - 1, node = 1):
    if RIGHT < l or LEFT > r: return 0
    if LEFT <= l and r <= RIGHT: return tree[node]
    mid = (l + r) // 2
    return find(LEFT, RIGHT, l, mid, node * 2) + find(LEFT, RIGHT, mid + 1, r, node * 2 + 1)

# solve
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        b, c = min(b, c),max(b, c)
        print(find(b - 1, c - 1))
    elif a == 1:
        diff = c - arr[b - 1]
        modify(b - 1, diff)
        arr[b - 1] = c
