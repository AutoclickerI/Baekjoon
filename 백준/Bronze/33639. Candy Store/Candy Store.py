N,Q=map(int,input().split())
d={}
for _ in[0]*N:s=input();(a,*_),(b,*_)=s.split();d[a+b]=d.get(a+b)and'ambiguous'or s
for _ in[0]*Q:print(d.get(input(),'nobody'))