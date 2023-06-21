import sys
input = sys.stdin.readline

n, m = map(int, input().split())
keyword = {}

for _ in range(n):
    keyword[input().strip()] = 1

answer = len(keyword)

for _ in range(m):
    words = list(input().strip().split(','))
    for word in words:
        if word in keyword:
            if keyword[word] == 1:
                keyword[word] = 0
                answer -= 1
    print(answer)
        