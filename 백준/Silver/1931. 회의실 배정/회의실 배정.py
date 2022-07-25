n = int(input())
arr = []
for i in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))

arr = sorted(arr, key = lambda x: [x[1], x[0]])
ans = 1
start, end = arr[0][0], arr[0][1]
for i in range(1, n):
    s, e = arr[i]
    if end <= s:
        start, end = s, e
        ans += 1

print(ans)