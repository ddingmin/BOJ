from collections import deque
input = __import__('sys').stdin.readline

n, m = map(int, input().split())

container = [0] * (m + 1)
q = deque()
for _ in range(n):
    p, w = map(int, input().split()) # 우선순위, 무게
    q.append((p, w))
    container[p] += 1

level = m # 지금 넣어야 하는 우선순위
cost = 0
stack = [] # 적재될 곳

while q:
    p, w = q[0]
    if level == p: # 현재 우선순위와 같다면
        # 적재 대기
        temp = [q.popleft()]
        
        # 적재된 컨테이너의 무게가 더 작다면 temp에 잠깐 빼줌
        while 1:
            if stack and stack[-1][0] == level and stack[-1][1] < w:
                cost += stack[-1][1]
                temp.append(stack.pop())
            else: break
        # 무게순으로 정렬
        temp.sort()
        
        if len(temp) == 1: # 뺄 일이 없는 경우 (바로 적재)
            stack.append((p, w))
            cost += w
        else:
            # 순서를 맞추고 적재하는 경우
            while temp:
                cost += temp[-1][1]
                stack.append(temp.pop())
        
        # 현재 순위의 컨테이너가 모두 적재되었다면 순위 -= 1
        container[level] -= 1
        if container[level] == 0: level -= 1
        
    else:
        q.append(q.popleft())
        cost += w
print(cost)