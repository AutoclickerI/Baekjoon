N=int(input())
a=len(s:=input())
for i in range(N-1):
    a+=len(S:=input())+1
    for i,j in zip(s,S):
        if i==j:a-=1
        else:break
    s=S
print(a)