N,K=map(int,open(0))

*p,=range(K+1)
for i in range(2,K+1):
    if p[i]:
        p[i*i::i]=[0]*len(range(i*i,K+1,i))
p=[i for i in p[2:]if i]

s={1}
for i in p:
    t={*s}
    for v in s:
        while v<=N:
            t.add(v)
            v*=i
    s=t
print(len(s))