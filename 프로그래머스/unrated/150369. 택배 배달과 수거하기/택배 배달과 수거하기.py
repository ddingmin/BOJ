
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
def solution(cap, n, deliveries, pickups):
    answer = 0
    d = 0
    p = 0
    pos = n - 1

    for i in range(n - 1, -1, -1):
        d += deliveries[i]
        p += pickups[i]

        while d > cap or p > cap:
            d -= cap
            p -= cap
            answer += 2 * (pos + 1)
            pos = i

    if d > 0 or p > 0:
        answer += 2 * (pos + 1)

    return answer