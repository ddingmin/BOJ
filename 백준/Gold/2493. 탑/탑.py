# input
input = __import__('sys').stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = [0] * n

stack = [(n - 1, arr[-1])]
for k in range(2, n + 1):
    c = arr[n - k]
    if c >= stack[-1][1]:
        while 1:
            a, b = stack.pop()
            ans[a] = n - k + 1
            if stack and c >= stack[-1][1]: continue
            else: 
                stack.append((n - k, c))
                break
    else:
        stack.append((n - k, c))

print(*ans)