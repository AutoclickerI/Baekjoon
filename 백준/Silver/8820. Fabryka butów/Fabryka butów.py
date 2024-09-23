f=lambda:[*map(int,input().split())]
for t in[0]*f()[0]:
 N,K=f();p=f();s=sum(p[K:])
 for i in range(K,N):t=max(t,-s*(~i+K));s-=p[i]
 print(t)