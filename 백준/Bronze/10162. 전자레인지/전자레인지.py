# A, B, C : 5, 1, 10
t = int(input())

if t % 10 != 0: 
    print(-1)
    exit(0)
a = t // 300
t %= 300
b = t // 60
t %= 60
c = t // 10
t %= 10
if t == 0: print(a, b, c)
else: print(-1)