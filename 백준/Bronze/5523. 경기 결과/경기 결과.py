aScore,bScore = 0,0
for i in range(int(input())):
    a,b = map(int,input().split())
    if a > b:
        aScore += 1
    elif a < b:
        bScore += 1
print(aScore,bScore)