word = input()

reverse = word[::-1]

for i in range(len(word) // 2 + 1):
    if word[i] != reverse[i]:
        print("0")
        exit(0)
        
print("1")