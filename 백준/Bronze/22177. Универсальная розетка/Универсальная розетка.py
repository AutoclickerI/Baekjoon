I=lambda:map(int,input().split())
N,D,*A=I()
B=[]
for _ in[0]*N:
    *l,t=I()
    if t:A=*A,l
    else:B+=l,
f=1
for x,y in A:
    for p,q in B:
        if(x-p)**2+(y-q)**2==D*D:f=0
print('YNeos'[f::2])