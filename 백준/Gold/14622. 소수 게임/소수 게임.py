import heapq
input = __import__('sys').stdin.readline


# 소수 만들기
prime = [1] * 5000001
prime[0], prime[1] = 0, 0
for i in range(2, 5000001):
    # 소수라면 소수 체크 완료
    if prime[i] == 0: continue
    
    for j in range(2, 5000001):
        if i * j > 5000000: break
        prime[i * j] = 0

n = int(input())

dwScore, gsScore = 0, 0
dwSaid, gsSaid = [], []

for _ in range(n):
    a, b = map(int, input().split())
    
    # 대웅이가 말함
    
    # 소수가 아닌 경우
    if prime[a] == 0:
        if len(gsSaid) < 3: gsScore += 1000
        else: 
            temp = []
            for _ in range(3):
                temp.append(heapq.heappop(gsSaid))
            gsScore += -1 * temp[2]
            for _ in range(3):
                heapq.heappush(gsSaid, temp.pop())
    # 중복된 소수인 경우
    elif prime[a] == 2: dwScore -= 1000
    # 통과인 경우
    else:
        heapq.heappush(dwSaid, -1 * a)
        prime[a] = 2
        
    # 규성이가 말함
    # 소수가 아닌 경우
    if prime[b] == 0:
        if len(dwSaid) < 3: dwScore += 1000
        else: 
            temp = []
            for _ in range(3):
                temp.append(heapq.heappop(dwSaid))
            dwScore += -1 * temp[2]
            for _ in range(3):
                heapq.heappush(dwSaid, temp.pop())
    # 중복된 소수인 경우
    elif prime[b] == 2: gsScore -= 1000
    # 통과인 경우
    else:
        heapq.heappush(gsSaid, -1 * b)
        prime[b] = 2
        

if dwScore > gsScore:
    print("소수의 신 갓대웅")
elif gsScore == dwScore:
    print("우열을 가릴 수 없음")
else:
    print("소수 마스터 갓규성")