(a,b,c),*z=[map(int,i.split())for i in open(0)]
d={i:i for i in range(101)}
for s,e in z[:b]:d[s]=e
l=[1]*a
i=0
for[v]in z[b:]:l[i]=d[min(100,l[i]+v)];i=(i+(l[i]<100))%a
for i in range(a):print('Position of player',i+1,f'is {l[i]}.')