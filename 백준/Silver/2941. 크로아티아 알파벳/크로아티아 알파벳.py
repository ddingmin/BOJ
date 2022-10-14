input = __import__('sys').stdin.readline

word = input().strip()
cnt = len(word)
for i in range(1, len(word)):
    if word[i] == "=":
        if word[i - 1] == "c": cnt -= 1
        elif word[i - 1] == "s": cnt -= 1
        elif word[i - 1] == "z":
            if i - 2 >= 0 and word[i - 2] == "d":
                cnt -= 1
            cnt -= 1
    elif word[i] == "-":
        if word[i - 1] == "c":
            cnt -= 1
        elif word[i - 1] == "d":
            cnt -= 1
    elif word[i] == "j":
        if word[i - 1] == "l":
            cnt -= 1
        elif word[i - 1] == "n":
            cnt -= 1

print(cnt)
            