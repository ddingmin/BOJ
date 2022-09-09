input = __import__('sys').stdin.readline

n = input().strip()
cnt = [0] * 10
for c in n:
    cnt[int(c)] += 1

for i in range(1, len(cnt) + 1):
    print(str(10 - i) * cnt[-i], end = '')