string = input()
answer = ""
for i in string:
    if i.isupper():
        answer += i.lower()
    else:
        answer += i.upper()
print(answer)