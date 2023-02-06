def sol(arr):
    temp = 0
    for i in arr:
        if i < 40:
            temp += 40
        else:
            temp += i

    return temp // 5

# input
arr = [int(input()) for _ in range(5)]
print(sol(arr))