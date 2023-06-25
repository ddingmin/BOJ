# 11816
word = input()

if len(word) >= 2 and word[0:2] == '0x':
    print(int(word[2:], 16))
elif len(word) >= 1 and word[0] == '0':
    print(int(word[1:], 8))
else:
    print(int(word))