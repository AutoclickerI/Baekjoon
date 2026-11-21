_,*l=[[*map(int,i.split())]for i in open(0)]
while l:(N,M),n,*l=l;t=M%N;print(M//N%2*n[~t]or n[t])