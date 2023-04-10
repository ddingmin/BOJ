a, b = map(int, input().split())
b = 100 - b
if a * b / 100 >= 100:
    print(0)
else:
    print(1)