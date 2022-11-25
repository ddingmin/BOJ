def fail_fuction(pattern):
    table = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        flag = 0
        # 틀린 경우 j가 0이거나 시작이 일치할때까지 구했던 실패함수 참조하며 이동
        while pattern[j] != pattern[i] and j > 0:
            j = table[j - 1]

        # 일치한 경우 +1, 우측 이동
        if pattern[i] == pattern[j]:
            flag = 1
            table[i] = j + 1
            j += 1
        # 일치 하지 않은 경우 0
        else:
            if flag:
                return 0
            # table[i] = 0
    return table[-1]

def solve(value, size):
    if value == 0:
        return 1
    else:
        ans = size / (size - value)
        if ans == int(ans):
            return int(ans)
        return 1


word = input().strip()
while word != ".":
    print(solve(fail_fuction(word), len(word)))
    word = input().strip()