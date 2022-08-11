input = __import__('sys').stdin.readline

# input
n = int(input())


# 해당 배열이 감소하는 수 인지 확인
def check(i):
	global num
	if len(num) == 1: return 1
	if num[-2] > i: return 1
	else: return 0

num = []
ans = []
def dfs(depth):
	global num
	for i in range(10):
		num.append(i)
		if check(i):
			dfs(depth + 1)
			ans.append(int(''.join(str(x) for x in num)))
		num.pop()
	
dfs(0)
ans.sort()

# 감소하는 수는 1022개 존재 그외는 -1 출력
if n >= len(ans): print(-1)
else: print(ans[n])
