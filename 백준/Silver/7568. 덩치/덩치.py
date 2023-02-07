def sol(n, arr):
    answer = [1] * n
    for i in range(n):
        for j in range(n):
            if arr[i][0] < arr[j][0] and  arr[i][1] < arr[j][1]:
                answer[i] += 1
    
    return answer

# input
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
print(*sol(n, arr))