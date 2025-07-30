(a,b,c),*z=[map(int,i.split())for i in open(0)]
d=dict(z[:b])
l=[1]*a
i=0
for[v]in z[b:]:v=min(100,l[i:=i%a]+v);x=l[i]=d.get(v,v);i+=x<100
for i in range(a):print('Position of player',i+1,f'is {l[i]}.')