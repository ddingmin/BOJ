input = __import__('sys').stdin.readline

mbti = input().strip()
n = int(input())
cnt = 0
for _ in range(n):
    if mbti == input().strip(): cnt += 1
print(cnt)