n,*l=map(int,open(0))
l.sort()
c=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if l[k]-l[j]<l[j]-l[i]:
                continue
            if (l[j]-l[i])*2<l[k]-l[j]:
                break
            c+=1
print(c)