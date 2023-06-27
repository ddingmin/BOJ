while 1:
    n = int(input())
    if n == 0: break
    
    visit = [0] * (n + 1)
    line = list(input().split(','))
    for l in line:
        pages = list(map(int, l.split('-')))
        
        if len(pages) == 1:
            if 0 < pages[0] < n + 1:
                visit[pages[0]] = 1
        else:
            for i in range(int(pages[0]), int(pages[1]) + 1):
                if 0 < i < n + 1:
                    visit[i] = 1
    print(sum(visit))