def sim(s):
    d={}
    i=0
    r=[]
    for c in s:
        d[c]=d.get(c,i:=i+1)
        r+=d[c],
    return*r,

d={}
for i in[*open(0)][1:]:
    i=sim(i)
    d[i]=d.get(i,0)+1
print(sum(d[i]*~-d[i]>>1 for i in d))