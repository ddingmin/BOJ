def solution(players, callings):
    names = {}
    price = {}
    
    for i in range(1, len(players) + 1):
        names[players[i - 1]] = i
        price[i] = players[i - 1]
    
    for call in callings:
        # a가 b를 추월함
        a, b = call, price[names[call] - 1]
        price[names[a]], price[names[b]] = price[names[b]], price[names[a]]
        names[a], names[b] = names[b], names[a]
    answer = []
    for i in range(1, len(players) + 1):
        answer.append(price[i])
    
    return answer