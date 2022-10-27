from collections import deque
input = __import__('sys').stdin.readline

t = int(input())
for _ in range(t):
    pal = input().strip()
    q = deque(list(pal))
    wrong = 0
    wrong2 = 0
    
    while q:
        if q[0] == q[-1]:
            if len(q) == 1: q.pop()
            else:
                q.pop()
                q.popleft()
        else:
            if len(q) > 2:
                if q[1] == q[-1]:
                    wrong += 1
                    q.popleft()
                elif q[0] == q[-2]:
                    wrong += 1
                    q.pop()
                else:
                    wrong += 2
                    break
            else:
                wrong += 1
                break
            
    q = deque(list(pal))
    while q:
        if q[0] == q[-1]:
            if len(q) == 1: q.pop()
            else:
                q.pop()
                q.popleft()
        else:
            if len(q) > 2:
                if q[0] == q[-2]:
                    wrong2 += 1
                    q.pop()
                elif q[1] == q[-1]:
                    wrong2 += 1
                    q.popleft()
                else:
                    wrong2 += 2
                    break
            else:
                wrong2 += 1
                break
    
    wrong = min(wrong, wrong2)
    if wrong > 1: print(2)
    else: print(wrong)