t = int(input())

def solve():
    h, w, n = map(int, input().split())
    arr = [[0] * w for _ in range(h)]
    user = 1
    for j in range(w):
        for i in range(h):
            arr[i][j] = user
            if user == n:
                return str(i + 1) + ('0' * (2 - len(str(j + 1))) + str(j + 1))
            user += 1
            
for _ in range(t):
    print(solve())