N,K=input().split()
s={N}
for _ in[0]*int(K):
    tmp=set()
    for v in s:
        *x,=v
        for i in range(len(v)):
            for j in range(i+1,len(v)):
                x[i],x[j]=x[j],x[i]
                if x[0]!='0':
                    tmp.add(''.join(x))
                x[i],x[j]=x[j],x[i]
    s=tmp
print(max(s or[-1]))