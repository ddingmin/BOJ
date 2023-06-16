
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
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
def solution(users, emoticons):
    answer = [0, 0]
    data = [10 ,20, 30, 40]
    discount = []
    def dfs(temp, depth):
        if depth == len(temp):
            discount.append(temp[:])
            return
        for d in data:
            temp[depth] += d
            dfs(temp, depth + 1)
            temp[depth] -= d

    dfs([0] * len(emoticons), 0)

    for d in range(len(discount)):
        join, price = 0, [0] * len(users)
        for e in range(len(emoticons)):
            for u in range(len(users)):
                if users[u][0] <= discount[d][e]:
                    price[u] += emoticons[e] * (100 - discount[d][e]) / 100
        # print(price)
        for u in range(len(users)):
            if price[u] >= users[u][1]:
                join += 1
                price[u] = 0

        # 갱신
        if join >= answer[0]:
            if join == answer[0]:
                answer[1] = max(answer[1], sum(price))
            else:
                answer[1] = sum(price)
            answer[0] = join


    return answer
