# BOJ 2096

# input
n = int(input())
a, b, c = map(int, input().split())
mx1, mx2, mx3 = a, b, c
mi1, mi2, mi3 = a, b, c

for i in range(1, n):
	x, y, z = (map(int, input().split()))

	t1, t2, t3 = mx1, mx2, mx3
	mx1 = max(t1 + x, t2 + x)
	mx2 = max(t1 + y, t2 + y, t3 + y)
	mx3 = max(t2 + z, t3 + z)
	t1, t2, t3 = mi1, mi2, mi3
	mi1 = min(t1 + x, t2 + x)
	mi2 = min(t1 + y, t2 + y, t3 + y)
	mi3 = min(t2 + z, t3 + z)

print(max(mx1, mx2, mx3), min(mi1, mi2, mi3))