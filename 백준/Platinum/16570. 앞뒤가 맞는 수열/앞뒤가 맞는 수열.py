def fail_fuction(pattern):
    table = [0] * len(pattern)
    j = 0
    length = 0
    
    for i in range(1, len(pattern)):
        while pattern[j] != pattern[i] and j > 0:
            j = table[j - 1]

        if pattern[i] == pattern[j]:
            table[i] = j + 1
            j += 1
            length = max(length, table[i])
        else:
            table[j] = 0

    return table, length
    

def solve(table, length):
    cnt = 0
    for i in table:
        if i == length:
            cnt += 1
    return cnt

n = int(input())
word = list(map(int, input().split()))[::-1]


tb, lg = fail_fuction(word)
cnt = solve(tb, lg)

if lg:
    print(lg, cnt)
else:
    print(-1)

