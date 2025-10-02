d={}
for i in[*open(0)][1].split():d[int(i)]=d.get(int(i),0)+1
v=0
for i in d:
    d[i]-=1
    f=0
    for j in d:
        if d[j]:
            d[j]-=1
            if d.get(i-j,0):
                f=1
            d[j]+=1
    d[i]+=1
    v+=f*d[i]
print(v)