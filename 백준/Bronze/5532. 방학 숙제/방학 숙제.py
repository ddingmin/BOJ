L=input()
A=input()
B=input()
C=input()
D=input()

L=int(L)
A=int(A)
B=int(B)
C=int(C)
D=int(D)

k=0
i=0

while A>0:
    A=A-C
    k+=1


while B>0:
    B=B-D
    i+=1

day=0
if(k>i):
    day=L-k
else:
    day=L-i

print(day)