N,M,*l=map(int,open(v:=0).read().split())
d=[0]*M
for i in 0,*l:d[v:=(v+i)%M]+=1
print(sum(i*~-i//2for i in d))