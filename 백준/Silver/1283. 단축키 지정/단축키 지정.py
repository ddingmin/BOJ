import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

# input
n = int(input())
visit = {}

for _ in range(n):
    answer = None
    words = input().strip()
    word_list = list(words.split())
    for idx in range(len(word_list)):
        if word_list[idx][0].upper() not in visit:
            visit[word_list[idx][0].upper()] = 1
            word_list[idx] = '[' + word_list[idx][0] + ']' + word_list[idx][1:]
            answer = ' '.join(word_list)
            break

    if answer:
        print(answer)
        continue

    for idx in range(len(words)):
        if words[idx] == ' ':
            continue
        if words[idx].upper() not in visit:
            visit[words[idx].upper()] = 1
            answer = words[:idx] + '[' + words[idx] + ']' + words[idx + 1:]
            break
    if answer is None:
        answer = words
    print(answer)
