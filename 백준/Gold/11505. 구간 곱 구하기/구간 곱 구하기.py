import sys
import math
input = sys.stdin.readline
MOD = 1_000_000_007
n, m, k = map(int, input().split())
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
        trees[node] = arr[l]
        return
    
    mid = (l + r) // 2
    # 자식 노드 생성
    segtree_init(l, mid, node * 2)
    segtree_init(mid + 1, r, node * 2 + 1)
    # 내 노드값 생성
    trees[node] = (trees[node * 2] * trees[node * 2 + 1]) % MOD

# 시작 node는 1로 지정
segtree_init()

def segtree_update(index, value, l = 0, r = n - 1, node = 1):
    # index가 노드 범위에 속하지 않는 경우
    if not (l <= index <= r): return
    
    if l == r:
        trees[node] = value
        return

    mid = (l + r) // 2
    segtree_update(index, value, l, mid, node * 2)
    segtree_update(index, value, mid + 1, r, node * 2 + 1)
    # 값 갱신
    trees[node] = (trees[node * 2] * trees[node * 2 + 1]) % MOD

def segtree_find(LEFT, RIGHT, l = 0, r = n - 1, node = 1):
    # 찾으려는 범위에 포함되지 않는다면
    if r < LEFT or l > RIGHT:
        return 1
    # 찾으려는 범위 안에 포함
    if LEFT <= l and r <= RIGHT:
        return trees[node]
    # 애매하게 걸친 경우
    mid = (l + r) // 2
    return (segtree_find(LEFT, RIGHT, l, mid, node * 2) * segtree_find(LEFT, RIGHT, mid + 1, r, node * 2 + 1)) % MOD

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        # 기존값의 차이 구하기 & 갱신
        segtree_update(b - 1, c)
        arr[b - 1] = c
        
    elif a == 2:
        print(segtree_find(b - 1, c - 1))