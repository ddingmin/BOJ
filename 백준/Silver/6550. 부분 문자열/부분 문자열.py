def solve(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == len(s): return "Yes"
    else: return "No"
    
while 1:
    try:
        s, t = input().split()
        print(solve(s, t))
    except EOFError: break