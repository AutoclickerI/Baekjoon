t,*a=map(int,open(0).read().split())
while a:
 n,e=a[:2];x=a[2:2+e];a=a[2+e:];*q,=range(1,n+1)
 for p in x:q.remove(p);q=[p]+q
 print(q[-1])