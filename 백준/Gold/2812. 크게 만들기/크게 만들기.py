n, k = map(int, input().split())
number = list(input())

def solve(number, count):
    temp = []
    for i in range(len(number)):
        # 스택의 최상단 원소가 새로들어올 원소보다 작을 경우 빼내기.
        while temp and int(temp[-1]) < int(number[i]) and count < k:
            temp.pop()
            count += 1
        temp.append(number[i])
    # 그리디하게 모두 빼내고 더 빼내야할 경우
    # 가장 상단의 원소부터 차례로 빼내기
    while count < k:
        temp.pop()
        count += 1
    return "".join(map(str, temp))

print(solve(number, 0))
