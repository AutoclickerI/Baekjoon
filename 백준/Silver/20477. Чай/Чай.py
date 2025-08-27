(N,V,X,K),*l=[map(int,i.split())for i in open(0)]
T=[0]*N
A=T[:]
a=T[:]
*z,=range(N)
for i in z:T[i],A[i]=l[i]
z.sort(key=lambda i:T[i])
v=t=0
d=20
for i in z:
 if t<T[i]:d=max(20,d-K*(T[i]-t));t=T[i]
 if v<A[i]:w=V-v;d=(v*d+w*20)/V;v=V
 t+=(100-d)/X*v;d=100;v-=A[i];a[i]=t
print(*a)