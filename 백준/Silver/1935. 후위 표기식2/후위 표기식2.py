n = int(input())
sen = list(input())
for i in range(n):
    t = input()
    for j in range(len(sen)):
        if sen[j] == chr(i + 65):
            sen[j] = t

stack = []
for i in range(len(sen)):
    if sen[i] in ['+','-','*','/']:
        temp = stack.pop()
        if sen[i] == '+':
            stack.append(stack.pop() + temp)
        elif sen[i] == '-':
            stack.append(stack.pop() - temp)
        if sen[i] == '*':
            stack.append(stack.pop() * temp)
        elif sen[i] == '/':
            stack.append(stack.pop() / temp)
    else:
        stack.append(int(sen[i]))


print("{0:.2f}".format(stack[0]))