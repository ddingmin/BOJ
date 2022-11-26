def fail_fuction(pattern):
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
            table[j] = 0
    return table[-1]

def solve(value, size, cnt):
    return size * cnt - (value) * (cnt - 1)


word, n = input().split()
n = int(n)

print(solve(fail_fuction(word), len(word), n))
