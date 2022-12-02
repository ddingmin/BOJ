a, b, c = map(int, input().split())

def zegop(a, b, c):
    if b == 2:
        return (a * a) % c
    if b < 2:
        return a % c
    else:
        tmp = zegop(a, b // 2, c)
        if b % 2 == 0:
            return tmp * tmp % c
        else:
            return tmp * tmp * a % c

print(zegop(a, b, c))