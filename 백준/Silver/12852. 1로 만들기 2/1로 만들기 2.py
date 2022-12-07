from collections import deque
dp = [(0, 0)] * 1000001
N = int(input())

def check_range(a):
    return 0 < a < 1000001 and dp[a] == (0, 0)

q = deque()
q.append(1)

while q:
    current = q.popleft()
    if check_range(current * 3):
        dp[current * 3] = (dp[current][0] + 1, current)
        q.append(current * 3)
    if check_range(current * 2):
        dp[current * 2] = (dp[current][0] + 1, current)
        q.append(current * 2)
        
    if check_range(current + 1):
        dp[current + 1] = (dp[current][0] + 1, current)
        q.append(current + 1)
        
        
ans_arr = [N]   
ans, temp = dp[N]
ans_arr.append(temp)
while temp:
    temp = dp[temp][1]
    ans_arr.append(temp)

print(ans)
print(*ans_arr[:-1])