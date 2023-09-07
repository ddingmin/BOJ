import sys

input = sys.stdin.readline
prime = [1] * 100_001
prime[0], prime[1] = 0, 0
arr = []
ans = [0] * 100_004

for i in range(2, 100_001):
    if prime[i] == 0:
        continue
    arr.append(i)
    for j in range(2, 100_001):
        idx = i * j
        if idx > 100_000: break
        prime[idx] = 0

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        idx = arr[i] * arr[j]
        if idx > 100_003: break
        ans[idx] = 1

for _ in range(int(input())):
    n = int(input())
    for i in range(n, 100_003):
        if ans[i]:
            print(i)
            break
    