# input
input = __import__('sys').stdin.readline
n, k = map(int, input().split())
length = len(str(n))
arr = list(str(n))
visit = [[0 for _ in range(11)] for _ in range(1000001)]

ans = -1

def dfs(arr, depth):
    global ans
    if depth == k:
        v = int(''.join(str(x) for x in arr))
        ans = max(ans, v)
        return
    
    for i in range(length):
        for j in range(i + 1, length):
            at = arr.copy()
            at[i], at[j] =  at[j], at[i]
            v = int(''.join(str(x) for x in at))
            if visit[v][depth]: continue
            else:
                if at[0] != '0': 
                    dfs(at, depth + 1)
                    visit[v][depth] = 1

dfs(arr, 0)
print(ans)