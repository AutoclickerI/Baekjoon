(n,k),*l=[map(int,i.split())for i in open(0)]
x={}
for i,*j in l:x[i]=j
print(sorted(x.values())[::-1].index(x[k])+1)