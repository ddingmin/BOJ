import sys
input = sys.stdin.readline

n, x = map(int, input().split())

arr = list(map(int, input().split()))

_wsum = sum(arr[0:x])

s, e = 0, x - 1

ans = [_wsum, 1]

while e < len(arr) - 1:
    _wsum -= arr[s]
    s += 1
    e += 1
    _wsum += arr[e]

    if _wsum > ans[0]:
        ans[0] = _wsum
        ans[1] = 1
    elif _wsum == ans[0]:
        ans[1] += 1

if ans[0] == 0:
    print("SAD")
else:
    print(ans[0])
    print(ans[1])