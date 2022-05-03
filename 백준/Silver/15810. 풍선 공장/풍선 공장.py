input = __import__('sys').stdin.readline
n, m =  map(int, input().split())
arr = sorted(list(map(int,input().split())))
s = 0
e = arr[0] * m
mid = 0
temp = 0

def check(t):
    temp = 0
    for i in arr:
        temp += t // i
    return temp >= m

ans = 0
while s + 1 < e:
    mid = (s + e) // 2
    if (check(mid)):
        e = mid
        ans = mid
    else:
        s = mid
print(e)