f=lambda:map(int,input().split())
N,K,T=f()
t=0
for i,j in zip(f(),f()):
    t+=i
    if t+K>=j:
        t=max(t,j)+T
    else:
        t=t+K
print(t)