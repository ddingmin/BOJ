input = __import__('sys').stdin.readline

x, y = map(int, input().split())
if (y // x) % 2 == 0: ans = x + y % x
else: ans = y % x 
print(ans)