a=[0]*734
S=Z=X=C=V=B=0
T=367
for i in[*open(0)][1:]:
 t,s,e=map(eval,i.split())
 for d in range(s,e+1):a[t+d]+=1;B=max(B,e-s+1)
for d in range(1,T):
 p,q=a[d::T]
 if s:=p+q:Z+=1;X=max(X,s);f=p==q;C+=f;V=max(V,s*f)
print(Z,X,C,V,B)