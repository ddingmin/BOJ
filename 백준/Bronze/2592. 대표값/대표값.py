count = [0] * (1000 + 1)

sum_ = 0
for _ in range(10):
    num = int(input())
    sum_ += num
    count[num] += 1

print(sum_ // 10)
print(count.index(max(count)))