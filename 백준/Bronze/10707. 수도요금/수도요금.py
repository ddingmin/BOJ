a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

a_price = a * e
if e <= c:
    b_price = b
else:
    b_price = b + (e - c) * d
print(min(a_price, b_price))
