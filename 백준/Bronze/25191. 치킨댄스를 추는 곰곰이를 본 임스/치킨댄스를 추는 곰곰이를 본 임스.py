n = int(input())
a, b = map(int, input().split())

temp = b + a // 2
print(min(n, temp))