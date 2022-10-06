input = __import__('sys').stdin.readline
n, l, r, x = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = 0
def dfs(depth, idx, maxim, mini, diff):
    global ans
    if diff > r: return
    elif depth >= 2 and l <= diff <= r:
        if not(maxim == None or mini == None) and maxim - mini >= x: ans += 1
    for i in range(idx, len(arr)):
        if mini == None: dfs(depth + 1, i + 1, arr[i], arr[i], diff + arr[i])
        else: dfs(depth + 1, i + 1, arr[i], mini, diff + arr[i])
dfs(0, 0, None, None, 0)
print(ans)