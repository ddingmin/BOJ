def fail_function(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        # 틀린 경우 j가 0이거나 시작이 일치할때까지 구했던 실패함수 참조하며 이동
        while pattern[j] != pattern[i] and j > 0:
            j = table[j - 1]
        # 일치한 경우 +1, 우측 이동
        if pattern[i] == pattern[j]:
            table[i] = j + 1
            j += 1
        # 일치 하지 않은 경우 0
        else:
            table[i] = 0
    return table

t = input()
p = input()
t_length = len(t)
p_length = len(p)

# 실패함수 테이블 세팅
table = fail_function(p)

ans = []


j = 0
for i in range(t_length):
    while j > 0 and t[i] != p[j]:
        j = table[j - 1]
    if t[i] == p[j]:
        if(j == p_length - 1):
            start = i - p_length + 2
            ans.append(start)
            j = table[j]
        else:
            j += 1
            


print(len(ans))
print(*ans)
