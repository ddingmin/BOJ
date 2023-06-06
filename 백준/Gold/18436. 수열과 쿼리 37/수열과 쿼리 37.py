import sys
import math
input = sys.stdin.readline

# init
n = int(input())
H = 2 ** math.ceil(math.log2(n) + 1)
stree = [0] * (H)
arr = list(map(int, input().split()))


# solve
def is_odd(value):
    return value % 2

def init(l = 0, r = n - 1, node = 1):
    if l == r:
        if arr[l] % 2 == 1:
            stree[node] = [1, 0]
        else:
            stree[node] = [0, 1]
        return
    
    mid = (l + r) // 2
    init(l, mid, node * 2)
    init(mid + 1, r, node * 2 + 1)
    lnode = stree[node * 2]
    rnode = stree[node * 2 + 1]    
    stree[node] = [lnode[0] + rnode[0], lnode[1] + rnode[1]]

def update(index, odd_flag, l = 0, r = n - 1, node = 1):
    if not(l <= index <= r): return
    if odd_flag == 1:
        stree[node][0] += 1
        stree[node][1] -= 1
        
    else:
        stree[node][0] -= 1
        stree[node][1] += 1
        
    if l == r: return
    
    mid = (l + r) // 2
    update(index, odd_flag, l, mid, node * 2)
    update(index, odd_flag, mid + 1, r, node * 2 + 1)

def find(LEFT, RIGHT, l = 0, r = n - 1, node = 1):
    if LEFT > r or RIGHT < l: return [0, 0]
    if LEFT <= l and r <= RIGHT:
        return stree[node]
    mid = (l + r) // 2
    lnode = find(LEFT, RIGHT, l, mid, node * 2)
    rnode = find(LEFT, RIGHT, mid + 1, r, node * 2 + 1)
    return [lnode[0] + rnode[0], lnode[1] + rnode[1]]


# input
init()

m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    # 쿼리 변경
    if a == 1:
        if arr[b - 1] % 2 == c % 2: continue
        update(b - 1, is_odd(c))
        arr[b - 1] = c
    elif a == 2:
        odd, even = find(b - 1, c - 1)
        print(even)
    elif a == 3:
        odd, even = find(b - 1, c - 1)
        print(odd)
    