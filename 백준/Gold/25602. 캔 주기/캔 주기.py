from collections import deque
input = __import__('sys').stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
r = []
m = []
for _ in range(k):
    r.append(list(map(int, input().split())))
    
for _ in range(k):
    m.append(list(map(int, input().split())))

happy = 0
ans = 0

def find(day):
    global happy
    global ans
    
    # k번째 날이 되면 갱신
    if day == k:
        ans = max(ans, happy)
        return
    
    for i in range(n):
        # 랑이의 캔 탐색
        if a[i]:
            # day날에 i번째 캔을 먹어 캔의 갯수 -1, 행복도 더하기
            a[i] -= 1
            happy += r[day][i]
            
            # 메리의 캔 탐색
            for j in range(n):
                if a[j]:
                    a[j] -= 1
                    happy += m[day][j]
                    # 랑이와 메리의 캔을 골랐으므로 다음날 탐색
                    find(day + 1)
                    # 골랐던 메리 캔, 행복도 다시 돌려놓기
                    a[j] += 1
                    happy -= m[day][j]
            # 골랐던 랑이 캔, 행복도 다시 돌려놓기
            a[i] += 1
            happy -= r[day][i]

def solve():
    find(0)
    return ans
        
print(solve())
