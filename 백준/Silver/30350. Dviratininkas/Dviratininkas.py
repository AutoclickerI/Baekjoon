N,K,*l=map(int,open(0).read().split())
for _,i in sorted(zip(l,range(1,N+1)))[:~K:-1]:print(i)