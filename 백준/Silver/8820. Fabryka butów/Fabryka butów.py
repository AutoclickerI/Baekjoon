_,*l=[[*map(int,i.split())]for i in open(0)]
while l:
 t=0;(N,K),p,*l=l;s=sum(p[K:])
 for i in range(N-K):t=max(t,s*-~i);s-=p[i+K]
 print(t)