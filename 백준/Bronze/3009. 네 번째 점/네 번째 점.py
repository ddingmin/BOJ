arr1 = []
arr2 = []
for _ in range(3):
    x, y = map(int, input().split())
    arr1.append(x)
    arr2.append(y)

for i in range(3):
    if arr1.count(arr1[i]) == 1:
        x4 = arr1[i]
    if arr2.count(arr2[i]) == 1:
        y4 = arr2[i]
print(x4, y4)
