(a,b,c),*z=[map(int,i.split())for i in open(0)]
d=dict(z[:b])
l=[1]*a
T=i=0
for[v]in z[b:]:x=l[i]=d.get(*[min(100,l[i:=i%a]+v)]*2);i+=x<100
while T<a:print('Position of player',T+1,f'is {l[T]}.');T+=1