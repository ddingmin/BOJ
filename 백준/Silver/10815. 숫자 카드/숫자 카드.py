n = input()
card = set(list(input().split()))
t = input()
arr = list(input().split())
for i in arr:
    if i in card: print(1, end = " ")
    else: print(0, end = " ")