arr = []

def hash(x, y):
    return x // 3 * 3 + y // 3

visit_row = [[0] * 10 for _ in range(10)]
visit_col = [[0] * 10 for _ in range(10)]
visit_33 = [[0] * 10 for _ in range(10)]

for i in range(9):
    arr.append(list(map(int, list(input()))))
    for j in range(9):
        if arr[i][j]:
            visit_row[i][arr[i][j]] = 1
            visit_col[j][arr[i][j]] = 1
            visit_33[hash(i, j)][arr[i][j]] = 1
            
def dfs(count):
    x = count // 9
    y = count % 9

    if count == 81:
        for k in arr:
            for kk in k:
                print(kk, end = "")
            print()
        exit(0)
    
    for num in range(1, 10):
        if arr[x][y] == 0:
            if visit_row[x][num] or visit_col[y][num] or visit_33[hash(x, y)][num]: continue
            visit_row[x][num] = 1
            visit_col[y][num] = 1
            visit_33[hash(x, y)][num] = 1
            arr[x][y] = num
            dfs(count + 1)
            arr[x][y] = 0
            visit_row[x][num] = 0
            visit_col[y][num] = 0
            visit_33[hash(x, y)][num] = 0
        else:
            return dfs(count + 1)
    

dfs(0)