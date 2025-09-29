d={}
for i in[*open(0)][1:]:
    x,y=map(int,i.split())
    d[x]=d.get(x,set())
    d[x]|={y}

l=sorted(d)
mid=l[0]+l[-1]
for i,j in zip(l,l[::-1]):
    if i+j!=mid or d[i]!=d[j]:exit(print('NO'))
print(mid//2,end=mid%2*'.5')