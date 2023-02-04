while 1:
    a = input()
    ans = 0
    if a == '#':
        break
    for i in range(len(a)):
        if a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u':
           ans += 1
        if a[i] == 'A' or a[i] == 'E' or a[i] == 'I' or a[i] == 'O' or a[i] == 'U':
           ans += 1
    print(ans)
