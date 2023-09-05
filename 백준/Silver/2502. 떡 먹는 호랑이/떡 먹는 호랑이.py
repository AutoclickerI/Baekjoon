D,K=map(int,input().split())
a,b=(1,0),(0,1)
for _ in[0]*~-D:a,b=b,(a[0]+b[0],a[1]+b[1])
for i in range(1,10**6):
    if(K-a[0]*i)%a[1]==0:exit(print(i,(K-a[0]*i)//a[1],sep='\n'))