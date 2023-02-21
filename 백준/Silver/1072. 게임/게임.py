import math
def solve(x, y):
    target = math.floor(y * 100 / x) + 1
    if target >= 100:
        return -1
    start = 1
    end = x + 1
    
    while start < end:
        mid = (start + end) // 2
        temp = math.floor((y + mid) * 100 / (x + mid))
        if temp >= target:
            end = mid
        else:
            start = mid + 1
    return start

x, y = map(int, input().split())
print(solve(x, y))