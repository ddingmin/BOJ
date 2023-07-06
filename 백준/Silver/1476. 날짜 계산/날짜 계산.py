input = __import__('sys').stdin.readline

a, b, c = 1, 1, 1
year = 1

x, y, z = map(int, input().split())

while (a, b, c) != (x, y, z):
    a += 1
    b += 1
    c += 1
    year += 1
    if a == 16:
        a = 1
    if b == 29:
        b = 1
    if c == 20:
        c = 1

print(year)