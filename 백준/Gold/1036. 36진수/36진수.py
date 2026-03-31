N,*l,K=open(0)
d={}
for i in l:
    for j,v in enumerate(i[::-1],-1):
        d[v]=d.get(v,0)+36**j
del d['\n']
v='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sd=sorted('0123456789QAWSXEDCRFVTGBYHNUJMIKOLP',key=lambda i:(d.get(i,0)*(35-v.index(i)),-ord(i)))
for _ in[0]*min(int(K),35):
    c=sd.pop()
    d['Z']=d.get('Z',0)+d.get(c,0)
    if c in d:del d[c]
r=0
for i in d:
    if i<='9':
        r+=d[i]*int(i)
    else:
        r+=d[i]*(ord(i)-55)

def to_36(n):
    if n==0:
        return''
    return to_36(n//36)+v[n%36]

print(to_36(r)or'0')