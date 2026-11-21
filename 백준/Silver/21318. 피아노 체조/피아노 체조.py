n,l,_,*k=open(0)
*l,=map(int,l.split())
L=[i:=0]
while i<int(n):L+=[L[-1]+(l[i]<l[i-1])];i+=1
for i in k:p,q=map(int,i.split());print(L[q]-L[p])