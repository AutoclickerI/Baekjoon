_,s=open(0)
v='ah'*10**5
l=[0]
for i,j in zip(v,s):t=i==j;l+=l[-1]*t+t,
l+=0,
for i,j in zip(v[1:],s):t=i==j;l+=l[-1]*t+t,
print(max(l))