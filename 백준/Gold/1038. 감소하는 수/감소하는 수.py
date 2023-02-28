def solve(n):
    answer = []
    def dfs(depth, num):
        answer.append(int(num))
        for i in range(9, -1, -1):
            if num[-1] > str(i):
                dfs(depth + 1, num + str(i))
    
    for i in range(10):
        dfs(0, str(i))
    
    answer.sort()
    if n < len(answer): return answer[n]
    else: return -1


n = int(input())
print(solve(n))