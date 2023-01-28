import time
n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 1
end = 2_000_000_000

def is_answer(mid):
    temp = 0
    for i in arr:
        t = (i - mid)
        if t > 0:
            temp += t
    return temp

while start <= end:
    mid = (start + end) // 2
    tree = is_answer(mid)
    if tree >= m:
        start = mid + 1
    else:
        end = mid - 1
    # if start == end: break
print(end)
