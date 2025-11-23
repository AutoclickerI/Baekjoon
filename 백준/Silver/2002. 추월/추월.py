n,*l=open(0)
n=int(n)
orig={j:i for i,j in enumerate(l[:n])}
mov=l[n:]

d={}
for i in range(n):
    for j in range(i+1,n):
        if orig[mov[j]]<orig[mov[i]]:
            d[mov[i]]=1
print(sum(d.values()))