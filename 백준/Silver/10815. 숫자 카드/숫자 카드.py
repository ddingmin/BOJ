n = input()
card = set(list(map(int, input().split())))
t = input()
arr = list(map(int, input().split()))
for i in arr:
    if i in card: print(1, end = " ")
    else: print(0, end = " ")