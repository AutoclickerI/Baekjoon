N,K=map(int,input().split())
l=[N]
v=[-1]*7**7
p=v[:]
v[N]=I=0
while l[I]-K:
 t=l[I];I+=1
 for i in t-1,t+1,2*t:
  if 7**7>i>=0>v[i]:v[i]=v[t]+1;p[i]=t;l+=i,
t,*a=v[K],
while~K:a+=K,;K=p[K]
print(t,*a[::-1])