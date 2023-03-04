n = int(input())
stack = []
max = 0
ans = []
flag = True
for i in range(n):
    t = int(input())
    if len(stack) == 0:
        if max == 0:
            for j in range(t):
                stack.append(j+1)
                ans.append('+')
            max = stack.pop()
            ans.append('-')
        else:
            for j in range(t-max):
                stack.append(max + 1 + j)
                ans.append('+')
            max = stack.pop()
            ans.append('-')
    elif t == stack[-1]:
        stack.pop()
        ans.append('-')
    elif t > stack[-1]:
        for k in range(t-max):
            stack.append(max + 1 + k)
            ans.append('+')
        max = stack.pop()
        ans.append('-')
    else: 
        flag = False
    
if flag:
    print("\n".join(ans))
else: print('NO')