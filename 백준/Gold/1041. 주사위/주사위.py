# BOJ 1041

n = int(input())

dice = list(map(int, input().split()))

a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] 
min1 = min(dice)
side_2 = [(a, b), (a, c), (a, d), (a, e), (b, d), (e, d), (e, c), (c, b), (d, f), (b, f), (c, f), (e, f)]
min2 = sum(side_2[0])
for i, j in side_2:
	min2 = min(min2, i + j)

side_3 = [(a, b, c), (a, c, e), (a, d, b), (a, e, d), (d, f, b), (b, f, c), (c, f, e), (e, f, d)]
min3 = sum(side_3[0])
for i, j, k in side_3:
	min3 = min(min3, i + j + k)

ans = 0
ans += (4 * (n - 1) * (n - 2) + (n - 2) * (n - 2)) * min1
ans += ((n - 1) * 4 + (n - 2) * 4) * min2
ans += 4 * min3
if n == 1: ans = sum(dice) - max(dice)
print(ans)