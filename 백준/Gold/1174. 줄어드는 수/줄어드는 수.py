# from collections import deque
input = __import__('sys').stdin.readline

# 1174 줄어드는 수

# input
n = int(input())
ans = []
def dfs(num):
    if len(num) > 1:
        # num이 비어있지 않을 때 줄어드는 수가 아니라면 반환
        if num[-2] <= num[-1]:
            return
    # 줄어드는 수가 존재하면 정답 배열에 넣기
    if num: ans.append(int(''.join(str(x) for x in num)))
    
    for i in range(10):
        num.append(i)
        dfs(num)
        num.pop()

dfs([])
ans.sort()
if len(ans) < n: print(-1)
else: print(ans[n - 1])