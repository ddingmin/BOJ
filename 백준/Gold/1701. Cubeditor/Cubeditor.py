word = input()
n = len(word)
table = [0] * len(word)

ans = 0

for _ in range(n):
    table = [0] * len(word)
    j = 0

    for i in range(1, len(word)):
        # 틀린 경우 j가 0이거나 시작이 일치할때까지 구했던 실패함수 참조하며 이동
        while word[j] != word[i] and j > 0:
            j = table[j - 1]
        
        # 일치한 경우 +1, 우측 이동
        if word[i] == word[j]:
            table[i] = j + 1
            j += 1
            # 답 갱신
            ans = max(ans, table[i])
        # 일치 하지 않은 경우 0
        else:
            table[i] = 0

    # 문자열을 하나씩 줄여나가며 모두 탐색
    word = word[1:]

print(ans)