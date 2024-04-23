[n],l=map(str.split,open(0))
n=int(n)
m=0
for i in range(1,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            m=max(m,eval('+'.join('*'.join(s)for s in[l[:i],l[i:j],l[j:k],l[k:]])))
print(m)