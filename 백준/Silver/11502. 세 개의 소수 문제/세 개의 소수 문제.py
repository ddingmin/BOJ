def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False

    return [x for x in range(limit + 1) if primes[x]]

def find_three_primes(num, primes):
    n = len(primes)

    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if primes[i] + primes[j] + primes[k] == num:
                    # 세 소수 출력
                    print(primes[i], primes[j], primes[k])
                    return

    # 불가능한 경우 0 출력
    print(0)

if __name__ == "__main__":
    t = int(input())  # 테스트 케이스의 수
    max_num = 1000  # 주어진 범위 내의 최댓값 (임의로 지정)

    # 에라토스테네스의 체로 소수 리스트 구하기
    primes = sieve_of_eratosthenes(max_num)

    for _ in range(t):
        k = int(input())  # 홀수 입력

        # 세 소수를 찾는 함수 호출
        find_three_primes(k, primes)
