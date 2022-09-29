input = __import__('sys').stdin.readline

#a, b, c = map(int,input().split())
a = int(input())

for i in range(1,10):
    print(a,"*",i,"=",a*i)
