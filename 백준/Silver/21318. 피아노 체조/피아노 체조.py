n,l,_,*k=open(0)
*l,=map(int,l.split())
L=[0]
for i in range(1,int(n)):L+=[L[-1]+(l[i]<l[i-1])]
for i in k:p,q=map(int,i.split());print(L[q-1]-L[p-1])