string = input()
answer = []
isOpen = False
temp = ""
for i in range(len(string)):
    if isOpen and string[i] == '>':
        temp += string[i]
        if temp:
            answer.append(temp)
            temp = ""
        isOpen = False
    
    elif not isOpen and string[i] == '<':
        if temp:
            answer.append(temp[::-1])
            temp = ""
            
        isOpen = True
        temp += string[i]
    elif string[i] == " " and not isOpen:
        if temp:
            answer.append(temp[::-1])
            temp = ""
            answer.append(" ")
    else:
        temp += string[i]
if temp:
    answer.append(temp[::-1])

print("".join(answer))