A,B=open(0,'rb')
d={}
c=z=l=a=0
for i in A[:-1]:c-=i%2*2-1;l|=c<0;d[c]=d.get(c,0)+1-l
for i in B:z-=i%2*2-1;l=min(l,z);a+=(z==l)*d.get(-z,0)
print(a)