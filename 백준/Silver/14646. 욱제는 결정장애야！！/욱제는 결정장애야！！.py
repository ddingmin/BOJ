# input
input = __import__('sys').stdin.readline
n = int(input())
arr = list(map(int, input().split()))

cnt = 0
visit = [0] * 1000000
ans = 0
for k in arr:
    if visit[k] == 0:
        cnt += 1
    elif visit[k] == 1:
        cnt -= 1
    visit[k] += 1
    ans = max(ans, cnt)
print(ans)