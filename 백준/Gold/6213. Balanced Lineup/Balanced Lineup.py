import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
# 세그 트리의 높이 지정
H = math.ceil(math.log(n, 2) + 1)
trees = [0] * (2 ** H)

arr = []
for _ in range(n):
    arr.append(int(input()))

# l ~ r 까지의 구간
def segtree_init(l = 0, r = n - 1, node = 1):
    # leaf 노드 경우
    if l == r:
        trees[node] = [arr[l], arr[l]]
        return
    
    mid = (l + r) // 2
    # 자식 노드 생성
    segtree_init(l, mid, node * 2)
    segtree_init(mid + 1, r, node * 2 + 1)
    # 내 노드값 생성
    trees[node] = [min(trees[node * 2][0], trees[node * 2 + 1][0]), max(trees[node * 2][1], trees[node * 2 + 1][1])]

# 시작 node는 1로 지정
segtree_init()

def segtree_find(LEFT, RIGHT, l = 0, r = n - 1, node = 1):
    # 찾으려는 범위에 포함되지 않는다면
    if r < LEFT or l > RIGHT:
        return [float('inf'), -float('inf')]
    # 찾으려는 범위 안에 포함
    if LEFT <= l and r <= RIGHT:
        return trees[node]
    # 애매하게 걸친 경우
    mid = (l + r) // 2
    left_node = segtree_find(LEFT, RIGHT, l, mid, node * 2)
    right_node = segtree_find(LEFT, RIGHT, mid + 1, r, node * 2 + 1)
    return [min(left_node[0], right_node[0]), max(left_node[1], right_node[1])]

# answer
for _ in range(m):
    a, b = map(int, input().split())
    short, long = segtree_find(a - 1, b - 1)
    print(long - short)