prime = [1] * 300000
prime[0] = 0
prime[1] = 0

for i in range(2, len(prime)):
    if prime[i] == 1:
        for j in range(2, len(prime)):
            if i * j >= 300000: break
            prime[i * j] = 0

while True:
    inn = int(input())
    if inn == 0: break
    cnt = 0
    for i in range(inn + 1, 2 * inn + 1):
        if prime[i]: cnt += 1
    print(cnt)