input = __import__('sys').stdin.readline

def check(a, b):
    if a > b:
        l, s = a, b
    else:
        s, l = a, b
    if s == l[:len(s)]: return 0
    return 1

t = int(input())
ans = ["YES"] * t
for case in range(t):
    # Input
    n = int(input())
    arr = []
    for i in range(n): arr.append(input().strip())
    # 일관성 비교를 위한 내림차순 정렬
    arr = sorted(arr, reverse = 1)
    
    # 비교
    stack = []
    for i in range(n):
        if not stack:
            stack.append(arr[i])
        else:
            # 길이가 작을때만 비교
            if len(arr[i]) < len(stack[-1]):
                for j in range(len(stack)):
                    flag = check(arr[i], stack[j])
                    if not flag: ans[case] = "NO"
                    stack.append(arr[i])
            # 길이가 작지 않다면 이전 값들을 더이상 비교할 필요가 없음
            else:
                stack = [arr[i]]
# Output
for k in ans: print(k)