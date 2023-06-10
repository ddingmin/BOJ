import sys
from math import ceil, log2
input = sys.stdin.readline

# init
n = int(input())
arr = list(map(int, input().split()))
H = 2 ** ceil(log2(n) + 1)
tree = [0] * H

# func
def init(l = 0, r = n - 1, node = 1):
    if l == r:
        tree[node] = [arr[l], l]
        return
    
    mid = (l + r) // 2
    init(l, mid, node * 2)
    init(mid + 1, r, node * 2 + 1)
    tree[node] = sorted([tree[node * 2], tree[node * 2 + 1]])[0]
    
def modify(index, value, l = 0, r = n - 1, node = 1):
    if not (l <= index <= r): return
    mid = (l + r) // 2
    if l == r:
        tree[node] = [value, l]
        return
    modify(index, value, l, mid, node * 2)
    modify(index, value, mid + 1, r, node * 2 + 1)
    tree[node] = sorted([tree[node * 2], tree[node * 2 + 1]])[0]
    
def find(LEFT, RIGHT, l = 0, r = n - 1, node = 1):
    if r < LEFT or RIGHT < l:
        return [float('inf'), float('inf')]
    if LEFT <= l and r <= RIGHT:
        return tree[node]
    mid = (l + r) // 2
    lnode = find(LEFT, RIGHT, l, mid, node * 2)
    rnode = find(LEFT, RIGHT, mid + 1, r, node * 2 + 1)
    return sorted([lnode, rnode])[0]

# solve
init()
for _ in range(int(input())):
    inst = list(map(int, input().split()))
    
    if inst[0] == 1:
        modify(inst[1] - 1, inst[2])
    elif inst[0] == 2:
        _, ans = find(0, n)
        print(ans + 1)