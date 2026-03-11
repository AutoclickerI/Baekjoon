d=['1110111','0010010','1011101','1011011','0111010','1101011','1101111','1010010','1111111','1111011']
cmap=[0]*100
for i in range(10):
    for j in range(10):
        cmap[i*10+j]=sum(map(str.__ne__,d[i],d[j]))

N,K,P,X=map(int,input().split())
X=str(X).zfill(K)
r=0
for i in range(1,N+1):
    p=str(i).zfill(K)
    v=sum(cmap[int(x)*10+int(y)]for x,y in zip(X,p))
    if 0<v<=P:
        r+=1
print(r)