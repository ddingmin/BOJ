import math

for _ in range(int(input())):
    ans = 0
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            ans = max(ans, math.gcd(arr[i], arr[j]))

    print(ans)
    