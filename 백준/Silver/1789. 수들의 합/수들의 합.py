n = int(input())

cnt = 0
temp = 0
for i in range(1, 10 ** 100):
    if i + temp > n: break
    else:
        cnt += 1
        temp += i
    
print(cnt)