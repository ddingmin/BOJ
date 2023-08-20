for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = 0
    for i in range(a, b + 1):
        word = str(i)
        for w in word:
            if w == '0':
                ans += 1
    print(ans)
