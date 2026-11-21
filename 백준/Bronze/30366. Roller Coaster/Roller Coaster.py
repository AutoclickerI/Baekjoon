N,M,*p=map(int,open(t:=0).read().split());L=M
for i in p:t+=L<i;L=[L,M][L<i]-i;print(t)