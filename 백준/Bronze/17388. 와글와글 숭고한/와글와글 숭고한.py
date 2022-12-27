arr = list(map(int, input().split()))
if sum(arr) < 100:
    if min(arr) == arr[0]:
        print("Soongsil")
    elif min(arr) == arr[1]:
        print("Korea")
    elif min(arr) == arr[2]:
        print("Hanyang")
else:
    print("OK")