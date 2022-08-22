from collections import deque

# input
input = __import__('sys').stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)

arrDown = []
arrUp = []
for k in arr:
    if k < 0: arrDown.append(k)
    else: arrUp.append(k)
arrDown = sorted(arrDown, reverse= True)
arrUp = sorted(arrUp)

ans = 0

if arrDown and arrUp:
    if abs(arrDown[-1]) > abs(arrUp[-1]):
        ans += abs(arrDown[-1])
        for _ in range(m):
            if arrDown: arrDown.pop()
    else:
        ans += abs(arrUp[-1])
        for _ in range(m):
            if arrUp: arrUp.pop()
elif arrDown and len(arrUp) == 0:
    ans += abs(arrDown[-1])
    for _ in range(m):
        if arrDown: arrDown.pop()
else:
    ans += abs(arrUp[-1])
    for _ in range(m):
        if arrUp: arrUp.pop()


while arrDown:
    ans += abs(arrDown[-1]) * 2
    for _ in range(m):
        if arrDown: arrDown.pop()

while arrUp:
    ans += abs(arrUp[-1]) * 2
    for _ in range(m):
        if arrUp: arrUp.pop()
    
print(ans)