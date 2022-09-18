input = __import__('sys').stdin.readline

n = int(input())
ans = 0
for _ in range(n):
    score = 0
    a, b, c = map(int, input().split())
    if a == b + c:
        score += 2 * a * (b + c)
    else:
        score += a * (b + c)
    ans = max(ans, score)
print(ans)