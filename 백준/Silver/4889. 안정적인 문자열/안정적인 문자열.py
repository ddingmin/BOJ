from collections import deque

input = __import__('sys').stdin.readline
num = 1
while 1:
    temp = input().strip()
    stack = []
    ans = 0
    for i in range(len(temp)):
        ch = temp[i]
        if ch == '-': exit(0)
        
        if ch == '{': 
            stack.append(ch)
        elif ch == '}':
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(ch)
    
    l, r = 0, 0
    for i in range(len(stack)):
        if stack[i] == '}':
            if l <= r: 
                ans += 1
                l += 1
            else: r += 1
        elif stack[i] == '{':
            l += 1
    ans += abs(l - r) // 2
    print(f"{num}.", ans)
    num += 1