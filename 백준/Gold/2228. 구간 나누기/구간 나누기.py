N,M,*l=map(int,open(0).read().split())

val_s=[-float('inf')]*M
idle_s=val_s+[0]
for i in l:
    val_t=[i+max(idle_s[j-1],val_s[j])for j in range(M)]
    idle_s=[max(p,q)for p,q in zip(val_s,idle_s)]+[0]
    val_s=val_t
print(max(val_s[-1],idle_s[-2]))