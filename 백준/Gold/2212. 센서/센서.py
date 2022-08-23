# input
input = __import__('sys').stdin.readline
n = int(input())
k = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

cnt = []
for i in range(1, n):
    cnt.append(arr[i] - arr[i - 1])
cnt = sorted(cnt)

for _ in range(k - 1):
    if cnt: cnt.pop()

print(sum(cnt))