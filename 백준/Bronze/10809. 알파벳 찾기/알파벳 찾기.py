answer = [-1] * 26
word = input()
for i in range(len(word)):
    if answer[ord(word[i]) - ord('a')] == -1:
        answer[ord(word[i]) - ord('a')] = i

print(*answer)