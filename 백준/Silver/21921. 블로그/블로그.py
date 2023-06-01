n,m,*l=map(int,open(0).read().split())
M=v=sum(l[:m])
c=1
e=m
while e<n:
    v+=l[e]-l[e-m]
    if v>M:M=v;c=0
    c+=(v==M);e+=1
print(f'{M} {c}'if M else'SAD')