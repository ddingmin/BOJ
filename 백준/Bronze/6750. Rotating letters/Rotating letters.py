need  = ['I', 'O', 'S', "H", "Z", "X", "N"]

word = str(input())

for i in word:
    if i not in need:
        print("NO")
        exit(0)

print("YES")
