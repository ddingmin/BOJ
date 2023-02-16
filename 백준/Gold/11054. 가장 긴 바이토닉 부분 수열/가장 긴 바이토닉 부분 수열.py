def solve(n, arr):
    dp = [0] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[j] + 1, dp[i])
    
    dp_back = [0] * n
    arr_back = arr[::-1]
    for i in range(1, n):
        for j in range(i):
            if arr_back[i] > arr_back[j]:
                dp_back[i] = max(dp_back[j] + 1, dp_back[i])

    answer = 0
    for i in range(n):
        answer = max(answer, dp[i] + dp_back[::-1][i])
    return answer + 1

# input
n = int(input())
arr = list(map(int, input().split()))
print(solve(n, arr))