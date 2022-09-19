# input
input = __import__('sys').stdin.readline

n = int(input())
# 부모를 담는 dic
dic = {}

for _ in range(n - 1):
    # a가 b의 자식
    a, b = input().split()
    if a not in dic: dic[a] = [b]
    else: dic[a].append(b)

# 질문
# a와 b가 부모 - 자식 관계인가?
a, b = input().split()

def find(c, f):
    flag = 0
    if c in dic:    # dic에 부모 관계를 찾음
        for k in dic[c]:    # 자식 관계를 탐색하면서 찾으려는 부모가 있는지 탐색
            if k == f:          # 찾으려는 부모 라면 1
                return 1
            else:               # 찾으려는 부모가 아니라면 현재 보고 있는 부모의 부모 관계를 탐색
                flag = find(k, f)
                return flag
    else:           # dic에 부모 관계가 없다면 0
        return 0

print(max(find(a, b), find(b, a)))