input = __import__('sys').stdin.readline

s = input().strip()
t = input().strip()

while len(t) > len(s):
    if t[-1] == "A":
        t = t[:len(t) - 1]
    else:
        t = t[:len(t) - 1]
        t = t[::-1]
if s == t: print(1)
else: print(0)