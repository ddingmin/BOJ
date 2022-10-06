from collections import deque

input = __import__('sys').stdin.readline

n, l, r, x = map(int, input().split())
arr = sorted(list(map(int, input().split())))
# 난이도를 오름차순 정렬시켜, 최소 난이도, 최대 난이도 갱신을 쉽게함.

ans = 0
def dfs(depth, idx, maxim, mini, diff):
    global ans
    if diff > r: return # 난이도의 합이 r보다 크면 안됨
    elif depth >= 2 and l <= diff <= r: # 선택된 문제가 2개 이상 and 난이도가 l과 r사이 
        if not(maxim == None or mini == None) and maxim - mini >= x: # 최고 난이도와 최저 난이도의 차이가 X이상
            ans += 1
    for i in range(idx, len(arr)):
        # 최소가 존재하지 않다면 (depth == 0) 최소값 지정
        # 최소가 존재하면 최소는 그대로, 최대 값만 갱신
        
        if mini == None:
            dfs(depth + 1, i + 1, arr[i], arr[i], diff + arr[i])
        else:
            dfs(depth + 1, i + 1, arr[i], mini, diff + arr[i])

dfs(0, 0, None, None, 0)
print(ans)