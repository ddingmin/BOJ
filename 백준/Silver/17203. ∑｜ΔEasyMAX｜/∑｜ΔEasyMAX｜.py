# input = __import__('sys').stdin.readline
n, q =  map(int, input().split())
arr = list(map(int, input().split()))

for i in range(q):
    x, y = map(int, input().split())
    ans = 0
    for j in range(x, y):
        ans += abs(arr[j] - arr[j-1])
    print(ans)


