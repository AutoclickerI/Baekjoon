d={}
for i in[*open(0)][2:]:
    a,v,h=map(int,i.split())
    p,q,r,s=d.get(a,(v,h,v,h))
    d[a]=(min(p,v),min(q,h),max(r,v),max(s,h))
p,q=min(((d[i][0]+~d[i][2])*(d[i][3]-d[i][1]+1),i)for i in d)
print(q,-p)