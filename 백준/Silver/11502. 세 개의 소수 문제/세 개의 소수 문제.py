*p,=range(1000)
for i in range(2,1000):
    if p[i]:p[2*i::i]=[0]*len(range(2*i,1000,i))

p={i for i in p if 1<i}

for i in[*open(0)][1:]:
    n=int(i)
    l=[3]
    n-=3
    for i in p:
        if n-i in p:
            l+=i,n-i
            break
    print(*sorted(l))