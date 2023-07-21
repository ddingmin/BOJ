import sys
input = sys.stdin.readline

count = [0, 0]

for _ in range(int(input())):
    count[int(input())] += 1

if count[0] > count[1]:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")