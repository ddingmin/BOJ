input = __import__('sys').stdin.readline

t = int(input())
for i in range(t):
    print('*' * (t - i))