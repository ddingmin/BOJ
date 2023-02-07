def gcd(a, b):
    while b != 0:
        n = a % b
        a = b
        b = n
    return a

def sol(a, b):
    temp = gcd(a, b)
    return [temp, a * b // temp]

# input
a, b = map(int, input().split())
for ans in sol(max(a, b), min(a, b)):
    print(ans)