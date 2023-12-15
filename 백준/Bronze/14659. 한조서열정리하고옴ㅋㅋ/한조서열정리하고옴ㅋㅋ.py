n,*l=map(int,open(0).read().split())
m=0
for i in range(n):
    t=0
    for j in l[i+1:]:
        if l[i]>j:
            t+=1
        else:
            break
    m=max(m,t)
print(m)