import sys
import math
input = sys.stdin.readline

# init
n = int(input())
arr = list(map(int, input().split()))
H = 2 ** math.ceil(math.log2(n) + 1)
tree = [0] * H

# code
def init(l = 0, r = n - 1, node = 1):
    if l == r:
        tree[node] = [arr[l], l]
        return
    mid = (l + r) // 2
    init(l, mid, node * 2)
    init(mid + 1, r, node * 2 + 1)
    lnode = tree[node * 2]
    rnode = tree[node * 2 + 1]
    if lnode[0] <= rnode[0]:
        tree[node] = lnode
    else:
        tree[node] = rnode
    
def modify(index, l = 0, r = n - 1, node = 1):
    if not(l <= index <= r): return 
    if l == r:
        tree[node] = [arr[l], l]
        return
    mid = (l + r) // 2
    modify(index, l, mid, node * 2)
    modify(index, mid + 1, r, node * 2 + 1)
    lnode = tree[node * 2]
    rnode = tree[node * 2 + 1]
    if lnode[0] <= rnode[0]:
        tree[node] = lnode
    else:
        tree[node] = rnode

def find(LEFT, RIGHT, l = 0, r = n - 1, node = 1):
    if RIGHT < l or LEFT > r: return [float('inf'), float('inf')]
    if LEFT <= l and r <= RIGHT: return tree[node]
    mid = (l + r) // 2
    
    lnode = find(LEFT, RIGHT, l, mid, node * 2)
    rnode = find(LEFT, RIGHT, mid + 1, r, node * 2 + 1)
    if lnode[0] <= rnode[0]:
        return lnode
    else:
        return rnode

# solve
init()
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 2:
        b, c = min(b, c),max(b, c)
        print(find(b - 1, c - 1)[1] + 1)
    elif a == 1:
        arr[b - 1] = c
        modify(b - 1)