A, B, C = map(int, input().split())
 
if (C - B) <= 0:
    print("-1")
else:
    N = A / (C - B)
    N = N + 1
    print(int(N))
    