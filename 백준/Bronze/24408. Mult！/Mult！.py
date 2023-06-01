N,n,*l=map(int,open(i:=0))
while i<N-1:
    if l[i]%n==0:print(l[i]);i+=1;n=i<N-1 and l[i]
    i+=1