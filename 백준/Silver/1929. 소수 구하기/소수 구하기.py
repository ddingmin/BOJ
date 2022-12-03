n, m = map(int, input().split())

prime = [0] * 1000001
prime[0] = 1
prime[1] = 1

# 에라토스테네스의 체
for i in range(2, 1000001):
    if prime[i]:
        continue
    else:
        for j in range(2, 1000001):
            if i * j > 1000000: break
            prime[i * j] = 1

for i in range(n, m + 1):
    if prime[i] == 0: print(i)