t = input()
st = []
ans = 0
for i in range(len(t)):
    if t[i] == '(':
        st.append(t[i])
    elif t[i] == ')':
        if t[i-1] == '(':
            st.pop()
            ans += len(st)
        else:
            ans += 1
            st.pop()
print(ans)
        