def solution(id_list, report, k):
    arr = []
    ans = {}
    for id in id_list:
        arr.append([id, []])
        ans[id] = 0
    for t in report:
        a, b = map(str, t.split())
        idx = id_list.index(b)
        arr[idx][1].append(a)
        arr[idx][1] = list(set(arr[idx][1]))

    for id, people in arr:
        if len(people) >= k: 
            for plusId in people: ans[plusId] += 1

    answer = []
    for a in ans.values():
        answer.append(a)

    print(answer)
    return answer