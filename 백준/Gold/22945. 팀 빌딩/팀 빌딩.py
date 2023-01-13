n = int(input())
arr = list(map(int, input().split()))

s = 0
e = n - 1

def calc(s, e):
    return (e - s - 1) * min(arr[s], arr[e])

# 시작값
answer = calc(s, e)
while s < e:
    answer = max(calc(s, e), answer)
    if arr[s] < arr[e]:
        s += 1
    else:
        e -= 1
print(answer)