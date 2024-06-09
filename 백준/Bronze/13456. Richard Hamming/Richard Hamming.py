_,*l=open(0).read().split()
while l:n=int(l.pop(0));print(sum(i!=j for i,j in zip(l[:n],l[n:])));l=l[2*n:]