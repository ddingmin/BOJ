# input
input = __import__('sys').stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = [0] * n

for i in range(n):
    cnt = 0
    target = arr[i]
    for j in range(n):
        if cnt == target and ans[j] == 0:
            ans[j] = i + 1
            break
        elif ans[j] == 0:
            cnt += 1

print(*ans)