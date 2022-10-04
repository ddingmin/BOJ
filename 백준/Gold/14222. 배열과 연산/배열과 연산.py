n, k = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse = True)

check = [0] * (n + 1)

for i in range(n):
    s = 0
    temp = arr[i]
    while arr[i] + s * k <= n:
        temp = arr[i] + s * k
        if 0 < temp < n + 1 and check[temp] == 0: break
        s += 1
    if 0 < temp < n + 1 and check[temp] == 0: check[temp] = 1
    else:
        print(0)
        exit(0)
print(1)
