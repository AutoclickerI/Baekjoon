l=[]
p,q,r,s=map(int,input().split())
i=j=k=0
while p*i<=s:
    while q*j<=s:
        while r*k<=s:
            l+=(p*i+q*j+r*k==s)*[(i,j,k)]
            k+=1
        k=0
        j+=1
    j=0
    i+=1
if l:
    for i in l:print(*i)
else:
    print('impossible')