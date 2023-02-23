import sys
input = sys.stdin.readline

def convert(text, i):
    temp = ""
    for c in text:
        temp += chr((ord(c) + i - ord('a')) % 26 + ord('a'))
    return temp

def solve(text, words):
    for i in range(26):
        for word in words:
            if word in convert(text, i):
                return convert(text, i)
    
    return -1

text = input().strip()
n = int(input())
words = [input().strip() for _ in range(n)]
print(solve(text, words))