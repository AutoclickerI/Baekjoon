m=10**9+7
N,*l=open(0,'rb')
v=[1]*26
t=[[]for _ in v]
for s,e,*_ in l:t[e-97]+=s-97,
print(sum(sum(v:=[sum(v[j]for j in i)%m for i in t])for _ in[0]*~-int(N.split()[1]))%m)