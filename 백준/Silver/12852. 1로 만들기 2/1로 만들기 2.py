d={0:(-1,0),1:(0,0),2:(1,1),3:(1,1)};n=int(input())
for i in range(1,n+1):
    a=[d[i//3][0]+i%3,d[i//2][0]+i%2,d[i-1][0]]
    if a.index(min(a))==0:
        if i%3==0:
            d[i]=(min(a)+1,i//3)
        else:
            d[i]=(min(a)+1,i-1)
    elif a.index(min(a))==1:
        if i%2==0:
            d[i]=(min(a)+1,i//2)
        else:
            d[i]=(min(a)+1,i-1)
    else:
        d[i]=(min(a)+1,i-1)
print(d[n][0])
print(n,end=' ')
while d[n][1]!=0:
    print(d[n][1],end=' ')
    n=d[n][1]