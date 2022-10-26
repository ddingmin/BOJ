input = __import__('sys').stdin.readline
# 약수 구하기
divisor = [0] * 1000001
divisor[1] = 1
for i in range(2, 1000001):
    for j in range(1, i + 1):
        if i * j < 1000001:
            if i == j:
                divisor[i * j] += j
            else:
                divisor[i * j] += j + i
        else:
            break

# 누적합 구하기
ans = [0] * 1000001
for i in range(1, 1000001):
    ans[i] += divisor[i] + ans[i - 1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(ans[n])