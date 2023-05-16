import sys
input = sys.stdin.readline

n, k = map(int, input().split())
visit = {}
num = n

answer = 1
while 1:
    mod = num % k
    if mod == 0:
        print(answer)
        break
    elif mod in visit:
        print(-1)
        break
    else:
        visit[mod] = True
        answer += 1
        num = int(str(mod) + str(n))
