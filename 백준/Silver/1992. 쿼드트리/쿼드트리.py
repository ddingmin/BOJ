def quad(size, arr, x, y):
    temp = arr[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if temp != arr[i][j]: return -1
    return temp

ans = ""
def solve(arr, size, x, y):
    global ans
    # 압축 가능한지 확인
    if size == 1 or quad(size, arr, x, y) > -1:
        ans += str(quad(size, arr, x, y))
        return
    else:
        ans += '('
        solve(arr, size // 2, x, y)
        solve(arr, size // 2, x, y + size // 2)
        solve(arr, size // 2, x + size // 2, y)
        solve(arr, size // 2, x + size // 2, y + size // 2)
        ans += ')'
    return ans

# input
n = int(input())
arr = [list(map(int, list(input()))) for _ in range(n)]

solve(arr, n, 0, 0)
print(ans)