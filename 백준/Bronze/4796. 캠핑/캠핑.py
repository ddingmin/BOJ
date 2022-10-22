day = 1
while 1:
    l, p, v = map(int, input().split())
    if l == p == v == 0: exit(0)
    ans = 0
    ans = v // p * l
    ans += min(v % p, l)
    print("Case {}: {}".format(day, ans))
    day += 1
