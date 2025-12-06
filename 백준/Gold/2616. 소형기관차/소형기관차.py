N,*l,c=map(int,open(0).read().split())
ps=[0]
for i in l:ps+=ps[-1]+i,
t1=[0]*c+[ps[c]-ps[0]]
for i in range(c+1,N+1):t1+=max(t1[-1],ps[i]-ps[i-c]),
t2=[0]*c+[ps[c]-ps[0]+t1[0]]
for i in range(c+1,N+1):t2+=max(t2[-1],ps[i]-ps[i-c]+t1[i-c]),
t3=[0]*c+[ps[c]-ps[0]+t2[0]]
for i in range(c+1,N+1):t3+=max(t3[-1],ps[i]-ps[i-c]+t2[i-c]),
print(t3[-1])