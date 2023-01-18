t = int(input())

for _ in range(t):
    n = input()
    arr = list(map(int, input().split()))
    sumfix = 0
    answer = max(arr)
    for i in arr:
        sumfix += i
        if sumfix < 0:
            sumfix = 0
            continue
        answer = max(answer, sumfix)
    print(answer)