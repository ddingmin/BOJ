import sys
input = sys.stdin.readline
LITTE = 0.000000001

n = int(input())
arr = [int(input()) for _ in range(n)]

if not arr:
    print(0)
else:
    arr = sorted(arr)
    no_check = round(n * 0.15 + LITTE)
    arr = arr[no_check:n - no_check]

    print(round(sum(arr) / len(arr) + LITTE))