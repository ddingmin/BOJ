import math

n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    ans = ""
    a, b = arr[0], arr[i]
    g = math.gcd(a, b)
    a, b = a // g, b // g
    ans = str(a) + "/" + str(b)
    print(ans)