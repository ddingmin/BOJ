import sys

input = sys.stdin.readline

# input
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def check(a, b):
    d = {}
    for i in a:
        d[i] = 1
    for i in b:
        if i in d:
            d[i] = 0

    temp = []

    for i in d.keys():
        if d[i] == 1:
            temp.append(i)
    return temp


ans = []
ans = ans + check(a, b)
ans = ans + check(b, a)
print(len(set(ans)))
