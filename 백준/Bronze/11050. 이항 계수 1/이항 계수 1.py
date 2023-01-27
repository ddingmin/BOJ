memo = [1] * 11
for i in range(2, 11):
    memo[i] = i * memo[i - 1]
n, k = map(int, input().split())
print(memo[n] // (memo[k] * memo[n - k]))