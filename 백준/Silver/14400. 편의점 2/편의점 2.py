from collections import deque
input = __import__('sys').stdin.readline

n = int(input())
aarr, barr = [], []
for _ in range(n):
	a, b = map(int, input().split())
	aarr.append(a)
	barr.append(b)
aarr.sort()
barr.sort()
a, b = aarr[n // 2], barr[n // 2]
ans = 0
for x, y in zip(aarr, barr):
	ans += abs(a - x)
	ans += abs(b - y)
print(ans)