week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
maxDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0

m, d = map(int, input().split())

for i in range(0, m - 1):
    day += maxDay[i]

answer = (day + d) % 7
print(week[answer])
