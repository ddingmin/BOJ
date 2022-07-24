t = int(input())
for cnt in range(1, t + 1):
    if cnt != 1: line = input()
    flag = True
    visit = [0] * 10
    arr = []
    for i in range(9):
        temp = list(map(int, input().split()))
        arr.append(temp)
        visit = [0] * 10
        for j in range(9):
            visit[arr[i][j]] += 1
        for k in range(1, 10):
            if visit[k] != 1: flag = False
    if not flag:
        print('Case {}: INCORRECT'.format(cnt))
        continue
    for i in range(9):
        visit = [0] * 10
        for j in range(9):
            visit[arr[j][i]] += 1
        for k in range(1, 10):
            if visit[k] != 1: flag = False
    if not flag:
        print('Case {}: INCORRECT'.format(cnt))
        continue

    check = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    for i, j in check:
        visit = [0] * 10
        for dx in range(3):
            for dy in range(3):
                visit[arr[i + dx][j + dy]] += 1
        for k in range(1, 10):
            if visit[k] != 1: flag = False

    if not flag:
        print('Case {}: INCORRECT'.format(cnt))
        continue
    else: print('Case {}: CORRECT'.format(cnt))