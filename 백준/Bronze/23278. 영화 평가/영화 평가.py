n,l,h=map(int,input().split())
s=sorted(list(map(int,input().split())))
print(sum(s[l:n-h])/(n-l-h))