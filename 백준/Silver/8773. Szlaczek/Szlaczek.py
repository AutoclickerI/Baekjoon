_,*l=[[*map(int,i.split())]for i in open(0)]
while l:(N,M),n,*l=l;r,q=divmod(M,N);print([n[q],n[~q]][r%2])