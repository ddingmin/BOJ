n = int(input())
for i in range(1, n+1):
    for j in range(n-i, 0, -1): print(" ", end='')
    print("*", end='')
    if i != 1:
        for j in range(i-1): print(" *", end='')
    print()
    
    