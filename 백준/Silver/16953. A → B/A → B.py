input = __import__('sys').stdin.readline
a, b = map(int, input().split())
cnt = 1
# a -> b 가 아닌 b -> a 로 가면서 가능한지 확인
# 즉 2로 나눌수 있다면 나누고, 나눌 수 없는 1 이 있는 경우엔 1을 제거하고 // 10 을 통해 b -> a
# 1이 아닌 홀수가 온다면 만들 수 없음.

while 1:
    # 정답이라면 출력
    if a == b:
        print(cnt)
        exit(0)
    # 1이라면 더이상 답을 구할 수 없으므로 -1
    if b == 1:
        print(-1)
        exit(0)
    
    # 가장 오른쪽에 1이 있다면 1을 제거하고 나누기 10
    if str(b)[-1] == '1':
        b = int(str(b)[0:-1])
    # 짝수라면 나누기 2
    elif b % 2 == 0: b //= 2
    # 1이 아닌 홀수면 불가능
    else: 
        print(-1)
        exit(0)
    cnt += 1
