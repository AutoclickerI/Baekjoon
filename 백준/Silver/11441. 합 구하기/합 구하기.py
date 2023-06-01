p,q,_,*r=open(0)
N,*l=map(int,(p+q).split())
l+=[0]
for i in range(N):l[i]+=l[i-1]
for i in r:p,q=map(int,i.split());print(l[q-1]-l[p-2])