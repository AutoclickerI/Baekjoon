n,*l,_=open(0)
v=[int(n)]
for a,b,_ in l:v+=8+(v[-1]+int(b)*(1-2*(a<'B')))%-8,
print(*v,'reject'*(len(v)<5or len(v)-len(set(v))))