input = __import__('sys').stdin.readline

# input
n, m = map(int, input().split())

print(n // m)
print(n % m)