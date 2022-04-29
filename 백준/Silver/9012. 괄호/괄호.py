n = int(input())
for i in range(n):
    t = input()
    
    flag = True
    st = []
    for j in range(len(t)):
        if t[j] == '(':
            st.append(t[j])
        else:
            if len(st) == 0 or st.pop() != '(':
                flag = False
                break
    if len(st) != 0: flag = False
    if flag: print('YES')
    else: print('NO')