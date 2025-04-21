(N,M,_),*l=[map(int,i.split())for i in open(0)]
s=N*M*[0]
for x,y,X,Y in l:
    for i in range(x-1,X):s[i*M+y-1:i*M+Y]=[1]*(Y-y+1)
print(sum(s))