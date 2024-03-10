N,M=map(int,input().split())
d={}
for _ in[0]*N:
    _,s,*l=input().split()
    t=''.join(l[:3])
    d[t]=d.get(t,[])+[s]
for _ in[0]*M:
    s=input().replace(' ','')
    t=d.get(s,'!')
    if len(t)==1:
        print(t[0])
    else:
        print('?')