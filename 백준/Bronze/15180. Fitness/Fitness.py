n,*l,_=open(0)
v=[int(n)]
for a,b,_ in l:v+=1+(v[-1]+int(b)*(-1)**(a<'B')-1)%8,
print(*v,'reject'*(len(v)<5 or len(v)-len(set(v))))