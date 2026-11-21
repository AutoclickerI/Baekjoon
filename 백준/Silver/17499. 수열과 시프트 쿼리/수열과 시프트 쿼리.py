(N,_),[*l],*Q=[map(int,i.split())for i in open(0)]
v=0
for q,i,*x in Q:
 if~-q:v+=i*(q*2-5)
 else:l[(i+v-1)%N]+=x[0]
print(*l[v%N:]+l[:v%N])