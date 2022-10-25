cnt = 0
n = input()
shouting = []
shouted = []
quack = [0] * 5
for i in range(len(n)):
    if n[i] == "q": 
        quack[0] += 1
        if not shouted: shouting.append(1)
        else: shouting.append(shouted.pop())
    elif n[i] == "u" and quack[0] > quack[1]:
        quack[1] += 1
    elif n[i] == "a" and quack[1] > quack[2]:
        quack[2] += 1
    elif n[i] == "c" and quack[2] > quack[3]:
        quack[3] += 1
    elif n[i] == "k" and quack[3] > quack[4]:
        quack[4] += 1
        shouted.append(shouting.pop())
    else:
        print(-1)
        exit(0)
if quack[0] != 0 and quack[0] == quack[1] == quack[2] == quack[3] == quack[4]:
    print(len(shouted))
else:
    print(-1)

