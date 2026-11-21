m=s=p=0
c=1
for i in[*open(0)][1].split():
    n=int(i)
    if n<p:
        c+=1
        s=1
    else:
        s+=1
    m=max(s,m)
    p=n
print(c,m)