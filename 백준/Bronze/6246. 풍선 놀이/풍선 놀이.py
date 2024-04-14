(N,_),*l=[map(int,i.split())for i in open(0)]
a=[]
for i,j in l:a+=range(i,N+1,j)
print(N-len({*a}))