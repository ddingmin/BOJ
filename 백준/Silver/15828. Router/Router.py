from collections import deque
input = __import__('sys').stdin.readline
n = int(input())
q = deque()
while 1:
	t = int(input())
	if t == -1:
		break
	elif t == 0:
		if q: q.popleft()
	elif len(q) < n:
		q.append(t)
if q: print(" ".join(map(str,q)))
else: print('empty')