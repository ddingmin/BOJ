input = __import__('sys').stdin.readline
x = int(input())
for a in sorted([int(input()) for _ in range(x)], reverse= 1): print(a)