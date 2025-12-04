N,M,*l=map(int,open(n:=0).read().split())
d=[0]*M
for i in 0,*l:d[n:=(n+i)%M]+=1;N-=d[n]
print(~N)