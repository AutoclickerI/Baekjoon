n,k,*t=map(int,open(0).read().split())
v=-k
for i in t:print(v:=max(v+k,i))