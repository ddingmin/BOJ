import heapq
input = __import__('sys').stdin.readline

n = int(input())
h = []

emsoo = dict()
yangsoo = dict()

for i in range(n):
    t = int(input())
    if t == 0:
        if h: 
            k = heapq.heappop(h)
            if emsoo[k] > 0:
                print(-k)
                emsoo[k] -= 1
            else:
                print(k)
                yangsoo[k] -= 1
        else: print(0)
    else:
        if abs(t) not in emsoo:
            emsoo[abs(t)] = 0
            yangsoo[abs(t)] = 0 
        if t < 0:
            emsoo[abs(t)] += 1
        elif t > 0:
            yangsoo[abs(t)] += 1

        heapq.heappush(h, abs(t))