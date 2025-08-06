_,*l=[map(int,i.split())for i in open(0)]
while l:
 (n,m),*l=l;x=[0]*n;y=x[:]
 for a,b,p,q in l[:m]:x[-a]+=p;y[-a]+=q;x[-b]+=q;y[-b]+=p
 p,*_,q=sorted(i+j and 1000*i*i//(i*i+j*j)for i,j in zip(x,y));print(q,p);l=l[m:]