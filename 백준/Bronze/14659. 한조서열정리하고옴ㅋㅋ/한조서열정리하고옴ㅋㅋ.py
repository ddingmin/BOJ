n=int(input())
arr=list(map(int,input().split()))

high=0
cnt=0
total=[]

for i in arr:
    if i>high:
        high=i
        cnt=0
    else:
        cnt+=1
    total.append(cnt)
print(max(total))