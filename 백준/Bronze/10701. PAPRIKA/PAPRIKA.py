(N,X),*b=[[*map(int,i.split())]for i in open(0)]
for i in range(N-1):
    if b[i][0]>b[i+1][0] and b[i][1]==1>0==b[i+1][1]:b[i][0],b[i+1][0]=b[i+1][0],b[i][0]
    elif b[i][0]<b[i+1][0] and b[i][1]==0<1==b[i+1][1]:b[i][0],b[i+1][0]=b[i+1][0],b[i][0]
c=0
for a,b in b:c+=a>X>0==b;c+=a<=X and b==1
print(c)