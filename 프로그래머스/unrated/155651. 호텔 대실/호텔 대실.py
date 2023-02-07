import heapq

def solution(book_time):
    time = []
    for bt in book_time:
        h, m = bt[0].split(':')
        s = int(h) * 60 + int(m)
        h, m = bt[1].split(':')
        e = int(h) * 60 + int(m) + 10
        time.append([s, e])
    time = sorted(time, key = lambda x: [x[0], x[1]])
    hq = []
    answer = 0
    for s, e in time:
        if not hq or hq[0][0] > e:
            heapq.heappush(hq, [e, s])
        else:
            while (hq and hq[0][0] <= s):
                heapq.heappop(hq)
            heapq.heappush(hq, [e, s])
        answer = max(answer, len(hq))
        
    return answer