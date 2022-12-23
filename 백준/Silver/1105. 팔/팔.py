L, R = input().split()
ans = 0
if len(L) == len(R):
    for i in range(min(len(L), len(R))):
        if L[i] != R[i]: break
        if L[i] == '8':
            ans += 1
print(ans)