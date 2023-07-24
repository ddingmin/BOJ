import sys
from collections import deque

input = sys.stdin.readline

d = {}

n = int(input())
for _ in range(n):
    word = input().strip()
    if word in d or word == word[::-1]:
        print(len(word), word[len(word) // 2])
    else:
        d[word[::-1]] = word[::-1]
