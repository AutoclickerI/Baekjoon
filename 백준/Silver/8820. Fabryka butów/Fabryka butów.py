f=lambda:[*map(int,input().split())]
for t in[0]*f()[0]:
 N,K=f();p=f();s=sum(p[K:])
 for i in range(N-K):t=max(t,s*(i+1));s-=p[i+K]
 print(t)