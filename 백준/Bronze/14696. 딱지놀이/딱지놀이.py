N = int(input())

for _ in range(N):
    temp_a = list(map(int, input().split()))[1:]  
    temp_b = list(map(int, input().split()))[1:]  

    for i in range(4, 0, -1):  
        if temp_a.count(i) > temp_b.count(i):  
            print("A")
            break
        elif temp_a.count(i) < temp_b.count(i): 
            print("B")
            break
        if i == 1:  
            print("D")  