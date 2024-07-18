n,w,h=map(int,input().split())
for i in range(n):
    leng=int(input())
    m=((w*w)+(h*h))**0.5
    if m>=leng:
        print('DA')
    else:
        print('NE')