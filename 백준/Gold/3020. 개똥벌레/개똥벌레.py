N,H,*l=map(int,open(0).read().split())
N>>=1
s=[0]*H
f=1
for i in l:f*=-1;s[f*i]-=f
d={}
for i in s:d[N]=d.get(N,0)+1;N+=i
print(m:=min(d),d[m])