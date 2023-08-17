import math

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    gcd = math.gcd(a, b)
    print(c // gcd)