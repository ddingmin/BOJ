N, K = map(int, input().split())
MAX_SIZE = N + 1
prime = [0] * MAX_SIZE
prime[0], prime[1] = -1, -1



cnt = 1
for i in range(2, MAX_SIZE):
    for j in range(1, MAX_SIZE):
        if i * j >= MAX_SIZE: break
        if prime[i * j] == 0:
            if cnt == K:
                print(i * j)
                exit(0)
            prime[i * j] = cnt
            cnt += 1
