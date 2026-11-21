(N,M),*l=[map(int,i.split())for i in open(0)]
x=[0]*N
for i,j in l:x[i-1]+=1;x[j-1]+=1
print(*x)