n = int(input())
arr = list(map(int, input().split()))
h = {}
for i in arr:
    h[i] = True
a = int(input())
check = list(map(int, input().split()))
for i in check:
    if i in h:
        print(1)
    else:
        print(0)