n = int(input())
arr = list(map(int, input().split()))
h = {}
for i in arr:
    if i in h:
        h[i] += 1
    else:
        h[i] = 1
a = int(input())
check = list(map(int, input().split()))
for i in check:
    if i in h:
        print(h[i], end = " ")
    else:
        print(0, end = " ")