import sys
from math import ceil, log

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

# input
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
H = 2 ** ceil(log(n, 2) + 1)
tree = [0] * H


# func
def init(l = 0, r = n - 1, node = 1):
    if l == r:
        tree[node] = arr[l]
        return

    mid = (l + r) // 2
    init(l, mid, node * 2)
    init(mid + 1, r, node * 2 + 1)
    tree[node] = min(tree[node * 2], tree[node * 2 + 1])


def find(LEFT, RIGHT, l = 0, r = n - 1, node = 1):
    if r < LEFT or RIGHT < l: return float('inf')
    if LEFT <= l and r <= RIGHT:
        return tree[node]
    mid = (l + r) // 2
    return min(find(LEFT, RIGHT, l, mid, node * 2),
               find(LEFT, RIGHT, mid + 1, r, node * 2 + 1))


# solve
init()
for _ in range(m):
    a, b = map(int, input().split())
    print(find(a - 1, b - 1))
