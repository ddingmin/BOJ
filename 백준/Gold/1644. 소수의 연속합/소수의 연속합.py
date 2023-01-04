import math
MAX_PRIME = 4_000_000
N = int(input())
prime = [1] * (MAX_PRIME + 1)
prime[0], prime[1] = 0, 0
for i in range(2, MAX_PRIME + 1):
    if prime[i] == 1:
        for mul in range(2, MAX_PRIME + 1):
            if mul * i < MAX_PRIME + 1:
                prime[mul * i] = 0
            else:
                break

subtotal = [0]
total = 0
for i in range(len(prime)):
    if prime[i] == 1:
        total += i
        subtotal.append(total)

answer = 0
L, R = 0, 1
while R < len(subtotal):
    total = subtotal[R] - subtotal[L]
    
    if total == N:
        answer += 1

    if total >= N:
        L += 1
    else:
        R += 1
print(answer)

