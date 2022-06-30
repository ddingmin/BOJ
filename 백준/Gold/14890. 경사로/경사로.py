n, l = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))


def check(road):
    use = [0] * n
    flag = True

    for i in range(0, n - 1):
        if road[i] == road[i + 1]: continue
        elif road[i] + 1 == road[i + 1]: # 1 1 1 2 2 2
            for k in range(l):
                if 0 <= i - k < n and use[i - k] == 0:
                    if road[i] == road[i - k]: continue
                flag = False
            if flag:
                for k in range(l):
                    use[i - k] = 1
        
        elif road[i] - 1 == road[i + 1]: # 3 2 2 1 1 1
            for k in range(l):
                if 0 <= i + 1 + k < n:
                    if road[i + 1] == road[i + 1 + k] and use[i + 1 + k] == 0: continue
                flag = False
            if flag:
                for k in range(l):
                    use[i + 1 + k] = 1
        
        else: flag = False
    
    return flag

ans = 0

for i in range(n):
    if check(arr[i]): ans += 1

arr = list(zip(*arr))

for i in range(n):
    if check(arr[i]): ans += 1

print(ans)
