line = input()
boom = input()

arr = []

for i in line:
    arr.append(i)
    if i == boom[-1] and boom == ''.join(arr[-len(boom):]):
        for _ in range(len(boom)):
            arr.pop()

if arr: print(''.join(arr))
else: print("FRULA")
