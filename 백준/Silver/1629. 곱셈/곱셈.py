a, b, c = map(int, input().split())

visit = [-1] * 1000000

def zegop(a, b, c):
    if b < 1000000 and visit[b] != -1:
        return visit[b]
    if b == 1 or b == 0:
        visit[b] = a % c
        return a % c
    if b % 2 == 0:
        if b < 1000000:
            visit[b] = (zegop(a, b // 2, c) * zegop(a, b // 2, c)) % c
        return (zegop(a, b // 2, c) * zegop(a, b // 2, c)) % c
    else:
        if b < 1000000:
            return (zegop(a, b // 2, c) * zegop(a, b // 2 + 1, c)) % c
        return (zegop(a, b // 2, c) * zegop(a, b // 2 + 1, c)) % c

print(zegop(a, b, c))