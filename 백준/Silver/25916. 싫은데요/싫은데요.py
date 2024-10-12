N,M=map(int,input().split())
*l,=map(int,input().split())
m=0
x=0
ptr1=ptr2=0
while ptr1<N:
    if x<M and ptr2<N:
        x+=l[ptr2]
        ptr2+=1
    else:
        x-=l[ptr1]
        ptr1+=1
    if x<=M:
        m=max(m,x)
print(m)