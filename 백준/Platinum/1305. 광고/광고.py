def fail_fuction(pattern):
    table = [0] * len(pattern)
    j = 0
    
    for i in range(1, len(pattern)):
        while pattern[j] != pattern[i] and j > 0:
            j = table[j - 1]

        if pattern[i] == pattern[j]:
            table[i] = j + 1
            j += 1
        else:
            table[j] = 0

    return table

n = int(input())
word = input().strip()

print(n - fail_fuction(word)[-1])